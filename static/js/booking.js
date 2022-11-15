document.addEventListener("DOMContentLoaded", function() {
    availableBookingSlot();
    $(document).on('change','select', () => availableBookingSlot());
    $("#id_date").on('change', () => availableBookingSlot());
});

async function availableBookingSlot() {
    response = await checkIfTableAvailble();
    if (response === false) {
        disableSubmitButton();
    } else {
        enableSubmitButton();
    }
}

async function checkIfTableAvailble() {
    const response = await axios.get("/booking/check/", {
        params: {
            date: $("#id_date").val(),
            time: $("#id_time option:selected").val(),
            tablesize: $("#id_tablesize option:selected").val(),
        }
    });
    console.log(response.data.tableAvailable);
    return response.data.tableAvailable;
}

function disableSubmitButton() {
    document.getElementById("no-booking").innerHTML = "Sorry, there are no available tables with this size at this time.";
    let noBooking = document.getElementById("no-booking");
    noBooking.classList.add("rounded");
    noBooking.classList.add("bg-danger");
    noBooking.classList.add("p-2");
    document.getElementsByClassName("submit-button")[0].disabled = true;
}

function enableSubmitButton() {
    document.getElementById("no-booking").innerHTML = "";
    let noBooking = document.getElementById("no-booking");
    noBooking.classList.remove("rounded");
    noBooking.classList.remove("bg-danger");
    noBooking.classList.remove("p-2");
    document.getElementsByClassName("submit-button")[0].disabled = false;
}

module.exports = { disableSubmitButton,enableSubmitButton };
