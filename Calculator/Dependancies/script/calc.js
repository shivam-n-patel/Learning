let input = document.getElementById('inputBox');
let buttons = document.querySelectorAll('.button');
let bodyEle = document.body;

let string = "";

buttons.forEach(button =>
{
    button.addEventListener
    ('click', (event) =>
        {
            if(event.target.innerHTML === '=')
            {
                string = eval(string);
                input.value = string;
            }

            else if(event.target.innerHTML === 'C')
            {
                string = "";
                input.value = string;
            }

            else if(event.target.innerHTML === 'DEL')
            {
                string = string.substring(0, string.length-1);
                input.value = string;
            }

            else
            {
                string += event.target.innerHTML;
                input.value = string;
            }
            
        }
    )
});


bodyEle.addEventListener
('keydown', (event) =>
    {
        var k = event.key;
        
        if (/[0-9+-/*%.]/.test(k))
        {
            string += k;
            input.value = string;
        }

        else if(k === 'Enter' || k === '=')
        {
            string = eval(string);
            input.value = string;
        }

        else if(['delete','d','backspace'].includes(k.toLowerCase()))
        {
            string = string.substring(0, string.length-1);
            input.value = string;
        }

        else if(k.toLowerCase() === 'c')
        {
            string = "";
            input.value = string;
        }
    }

);