$(document).ready(function () {
    // Click Function
    $('.bc_click').click(function(){
        alert("You clicked me lil bitch!!!");
    });
    // Hide Function
    $('button.bc_hide').click(function(){
        $('p.bc_hide').hide();
    });
    // Show Function
    $('.bc_show').click(function(){
        $('p.bc_hide').show();
    });
    // Toggle Function
    $('button.bc_toggle').click(function(){
        $('p.bc_toggle').toggle();
    });
    //Slide Down Function 
    $('h2.bc_slide').hide();
    $('button.bc_slide').click(function(){
        $('h2.bc_slide').slideDown();
    });
    //Slide Up Function
    $('button.bc_slideUp').click(function(){
        $('h2.bc_slideUp')slideUp();
    });
});