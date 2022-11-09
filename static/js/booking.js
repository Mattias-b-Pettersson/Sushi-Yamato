document.addEventListener("DOMContentLoaded", function() {
    availableBookingSlot()
    $(document).on('change','select', () => availableBookingSlot());
    $("#id_date").on('change', () => availableBookingSlot());
});

async function availableBookingSlot() {
    const response = await axios.get("/booking/check/", {
    params: {
    date: $("#id_date").val(),
    time: $("#id_time option:selected").val(),
    tablesize: $("#id_tablesize option:selected").val(),
    }
    })
    console.log(response.data)
    if (response.data.tableAvailable === false) {
        $(".submit-button").prop("disabled", true);
        $("#no-booking").text("Sorry, there are no available tables with this size at this time.");
        $("#no-booking").addClass("bg-danger p-2 rounded")
    } else {
        $(".submit-button").prop("disabled", false);
        $("#no-booking").removeClass("bg-danger p-2 rounded")
        $("#no-booking").text("");
    }
}