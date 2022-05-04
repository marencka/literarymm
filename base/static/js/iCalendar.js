/**
 * IMPORTANT: This code wasn't written by any of us. 
 * We used it as plug in for calendar for dashboard.html. 
 * However, we made changes to the styling in iCalendar.css 
 * to match overall aesthetics of the website
 * 
 * Source: https://github.com/nickknezevich/iCalendar
 */


/*
 * iCalendar v1.0-alpha
 *
 *
 * MIT License
 *
 * Copyright (c) 2019 Nikola Knezevic
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 */

class iCalendar {
    constructor(target) {
        if (!target) {
            throw new Error('iCalendar: Target argument missing!');
        } else {
            let elementExists = !!document.getElementById(target);
            if (elementExists == false) {
                throw new Error('iCalendar: Specified target does not exist in DOM');
            }
        }
        this.target = target;
        this.version = 'v1.0-alpha';
        this.months = {
            0: "January",
            1: "February",
            2: "March",
            3: "April",
            4: "May",
            5: "June",
            6: "July",
            7: "August",
            8: "September",
            9: "October",
            10: "November",
            11: "December"
        };
        this.today = new Date();
        this.currentMonth = this.today.getMonth();
        this.currentYear = this.today.getFullYear();
        this.selectYear = this.currentYear;
        this.selectMonth = this.currentMonth;
        this.selectedDate = null;
        this.calendarBody = document.querySelector('#cal-frame table.curr tbody');
        this.events = [];
        this.apiUrl = null;
        this.eventsJSON = [];
    }

    render() {
        let structure = '<div id="cal"><div class="header"><a href="" class="prev"><span class="left button" id="prev"> <span class="brackets">&lang;</span> </span></a><span class="month-year" id="label"> June 2020 </span><a href="" class="next"><span class="right button" id="next">  <span class="brackets">&rang;</span> </span></a></div>';
        structure += '<table id="days"><td>sun</td><td class="weekday">mon</td><td class="weekday">tue</td><td class="weekday">wed</td><td class="weekday">thu</td><td class="weekday">fri</td><td>sat</td></table>';
        structure += '<div id="cal-frame"><table class="curr"><tbody id="calendar-body"></tbody></table></div>';
        structure += '</div>';

        document.getElementById(this.target).innerHTML = structure;
        this.updateCalendar(this.currentMonth, this.currentYear);
        this._eventHandler();
    }

    updateCalendar(month, year) {
        let firstDay = (new Date(year, month)).getDay();
        let tbl = document.getElementById("calendar-body"); // body of the calendar

        // clearing all previous cells
        tbl.innerHTML = "";

        // filing data about month and in the page via DOM.
        let monthAndYear = document.getElementById('label');
        monthAndYear.innerHTML = this.months[month] + " " + year;
        //this.selectYear.value = year;
        //this.selectMonth.value = month;

        // creating all cells
        let date = 1;
        for (let calendarRow = 0; calendarRow < 6; calendarRow++) {
            // creates a table row
            let row = document.createElement("tr");

            //creating individual cells, filing them up with data.
            for (let callendarCell = 0; callendarCell < 7; callendarCell++) {
                if (calendarRow === 0 && callendarCell < firstDay) {
                    let cell = document.createElement("td");
                    cell.classList.add('nil');
                    let cellText = document.createTextNode("");
                    let div = document.createElement('div');
                    div.setAttribute('class', "day");
                    div.appendChild(cellText);
                    cell.appendChild(div);
                    row.appendChild(cell);
                } else if (date > this._daysInMonth(month, year)) {
                    break;
                } else {
                    let cell = document.createElement("td");
                    let cellText = document.createTextNode(date);
                    let div = document.createElement('div');
                    div.setAttribute('class', "day");
                    let a = document.createElement('a');
                    let actualMonth = this.currentMonth + 1;
                    a.setAttribute('data-id', this.currentYear + '-' + actualMonth + '-' + date);
                    a.setAttribute('class', 'calendarLink');
                    a.appendChild(cellText);
                    div.appendChild(a);
                    // color today's date
                    if (date === this.today.getDate() && year === this.today.getFullYear() && month === this.today.getMonth()) {
                        //cell.classList.add("bg-info");
                        div.classList.add('today');
                    }
                    //Check if date is weekend and apply styles
                    if (this._isWeekend(this.currentYear, this.currentMonth, date)) {
                        div.classList.add('weekend');
                    }
                    cell.appendChild(div);
                    row.appendChild(cell);
                    date++;
                }
            }
            tbl.appendChild(row); // appending each row into calendar body.
        }
    }

    next() {
        this.currentYear = (this.currentMonth === 11) ? this.currentYear + 1 : this.currentYear;
        this.currentMonth = (this.currentMonth + 1) % 12;
        this.updateCalendar(this.currentMonth, this.currentYear);
    }

    previous() {
        this.currentYear = (this.currentMonth === 0) ? this.currentYear - 1 : this.currentYear;
        this.currentMonth = (this.currentMonth === 0) ? 11 : this.currentMonth - 1;
        this.updateCalendar(this.currentMonth, this.currentYear);
    }

    jump() {
        currentYear = parseInt(selectYear.value);
        currentMonth = parseInt(selectMonth.value);
        showCalendar(currentMonth, currentYear);
    }

    _daysInMonth(iMonth, iYear) {
        return 32 - new Date(iYear, iMonth, 32).getDate();
    }

    _isWeekend(year, month, date) {
        var dt = new Date(year, month, date);
        if (dt.getDay() == 6 || dt.getDay() == 0) {
            return true;
        } else {
            return false;
        }
    }

    _eventHandler() {
        let prevButton = document.querySelector("a.prev");
        prevButton.addEventListener("click", event => {
            event.preventDefault();
            this.previous();
        });

        let nextButton = document.querySelector("a.next");
        nextButton.addEventListener("click", event => {
            event.preventDefault();
            this.next();
        });

        document.addEventListener('click', function(event) {
            if (event.target.classList.contains('calendarLink')) {
                //remove previously selected element
                let calendarLinks = document.getElementById('calendar-body').getElementsByClassName('selected-link');
                for (var i = 0; i < calendarLinks.length; i++) {
                    calendarLinks[i].classList.remove('selected-link');
                }
                //remove previously selected element
                let selectedElement = event.target;
                selectedElement.classList.add("selected-link");
                this.selectedDate = selectedElement.getAttribute("data-id");
                let cEvent = new Event("iCalendarDateSelected");
                document.dispatchEvent(cEvent);
                //this._fetchEvents();
                //console.log(this.selectedDate);
                event.preventDefault();
            }
        }.bind(this));
    }

    addEvent(iCalendarEvent) {
        this.events.push(iCalendarEvent);
    }

    getEvents() {
        return this.events;
    }

    setAPIUrl(apiURL) {
        this.apiUrl = apiURL;
    }

    _fetchEvents() {
        fetch(this.apiUrl + "?date=" + this.selectedDate).then(function(response) {
            // with the response, convert it to JSON, then pass it along
            response.json().then(function(json) {

            });
        });
    }

    _makeThisExtend(obj, CtorFunc) {
        for (var k in obj)
            if ({}.hasOwnProperty.call(obj, k))
                obj[k] = { value: obj[k] };
        return Object.create(CtorFunc.prototype, obj);
    }
}

class iCalendarEvent {
    constructor() {
        this.id = null;
        this.start = "";
        this.end = "";
        this.title = "";
        this.body = "";
        this.url = "";
        this.color = "";
    }
}

