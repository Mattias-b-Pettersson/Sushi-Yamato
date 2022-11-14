/**
 * @jest-environment jsdom
 */
const booking = require("../js/booking");


beforeEach(() => {
    document.body.innerHTML = "<p id='no-booking'></p><input class='btn btn-primary d-flex mx-auto px-3 submit-button' type='submit' value='Submit'>"
})

describe("Disable or enable submit button", () => {
    describe("Disable submit button", () => {
        test("Should fill p tag with text", () => {
            booking.disableSubmitButton()
            expect(document.getElementById("no-booking").innerHTML).toBe("Sorry, there are no available tables with this size at this time.")
            expect(document.getElementById("no-booking").classList.contains("bg-danger")).toBe(true)
        });
        test("Should add classes", () => {
            booking.disableSubmitButton()
            expect(document.getElementById("no-booking").classList.contains("bg-danger")).toBe(true)
            expect(document.getElementById("no-booking").classList.contains("rounded")).toBe(true)
            expect(document.getElementById("no-booking").classList.contains("p-2")).toBe(true)
        });
        test("Should add disable attribute button", () => {
            booking.disableSubmitButton()
            expect(document.getElementsByClassName("submit-button")[0].disabled).toEqual(true)
        });

    });
    describe("enable submit button", () => {
        test("Should delete text from p tag", () => {
            document.getElementById("no-booking").innerHTML = "hello";
            booking.enableSubmitButton();
            expect(document.getElementById("no-booking").innerHTML).toBe("");
        });
        test("Should remove classes", () => {
            booking.enableSubmitButton();
            expect(document.getElementById("no-booking").classList.contains("bg-danger")).toBe(false);
            expect(document.getElementById("no-booking").classList.contains("rounded")).toBe(false);
            expect(document.getElementById("no-booking").classList.contains("p-2")).toBe(false);
        });
        test("Should add disable attribute button", () => {
            booking.enableSubmitButton();
            expect(document.getElementsByClassName("submit-button")[0].disabled).toEqual(false);
        });
    });
});