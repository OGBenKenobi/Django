// Inside of .js file, use the following code to implement jquery commands:
    $(document).ready(function () {

        // jquery methods go here

    });

// Streamlined version of the above code:
    $(function(){

        // jQuery methods go here...
    
    });

// jquery commands are written inside of the {}. ex:
    $(document).ready(function(){
        $('h2').addClass('text-center');
        $('button').addClass('btn btn-danger');
        $('button.bc_click').click(function(){
            alert("OUCH!!!");
        });
    });

// Basic syntax is: 
    $(selector).method()
//     A $ sign to define/access jQuery
//     A (selector) to "query (or find)" HTML elements
//     A jQuery method() to be performed on the element(s)

// To select an element using jquery, use the following syntax:
    $('element')

// Followed by a function:
    $('h1').hide()
    
// Useful jquery selectors:
    // Selects all elements
        $("*")	
    // Selects the current HTML element	
        $(this)	
    // Selects all <p> elements with class="intro"	
        $("p.intro")	
    // Selects the first <p> element	
        $("p:first")
    // Selects the first <li> element of the first <ul>		
        $("ul li:first")
    // Selects the first <li> element of every <ul>		
        $("ul li:first-child")	
    // Selects all elements with an href attribute	
        $("[href]")
    // Selects all <a> elements with a target attribute value equal to "_blank"		
        $("a[target='_blank']")		
    // Selects all <a> elements with a target attribute value NOT equal to "_blank"
        $("a[target!='_blank']")
    // Selects all <button> elements and <input> elements of type="button"		
        $(":button")	
    // Selects all even <tr> elements	
        $("tr:even")	
    // Selects all odd <tr> elements	
        $("tr:odd")	

// List of functions you should get familiar with:
//     Effects (functions to do some cool animation effects)
        .hide()
        .show()
        .toggle()
        .slideUp() - not available in the slim version
        .slideDown() - not available in the slim version
        .slideToggle() - not available in the slim version
        .fadeOut() - not available in the slim version
        .fadeIn() - not available in the slim version
    // CSS (adding or removing a class for any HTML element/DOM)
        .addClass()
        .removeClass()
        .css()
    // Manipulation (retrieving or setting value or text in any HTML element)
        .after()
        .append()
        .prepend()
        .attr()
        .before()
        .html()
        .text()
        .val()
    // Events (functions to handle an event)
        .click()
        .on()
        .live() - deprecated (JQuery 1.7)
        .hover()

    // $(this) is used to select a particular element that triggered an event. Ex:
        $('img').click(function(){
            $(this).hide();
        });
    // the above code hides the very image that is clicked on a page