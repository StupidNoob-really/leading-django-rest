const ip = 'http://192.168.10.147:80'
// let input_last_name = document.getElementById('input_last_name')

// input_first_name.addEventListener('focusout', ()=>{check_input(input_first_name)})
// input_first_name.addEventListener('focusout', ()=>{check_input(input_last_name)})
// input_first_name.addEventListener('focusout', ()=>{check_input(input_father_name)})

let re_name = /^([А-Я]{1}[а-яё]{1,23})$/;
let re_phone = /^\+7\([0-9]{3}\)[0-9]{3}\-[0-9]{2}-[0-9]{2}$/;
let re_passport_serial = /^[0-9]{6}$/
let re_passport_number = /^[0-9]{4}$/
let mask_phone = {
	    mask: '+{7}(000)000-00-00',
	    lazy: false
	} 

let mask_passport_number = {
	    mask: '0000',
	    lazy: false
	} 

let mask_passport_serial = {
	    mask: '000000',
	    lazy: false
	} 

let element_ids = [
		{id: 'input_first_name', re: re_name, is_mask: false},
		{id: 'input_last_name', re: re_name, is_mask: false},
		{id: 'input_father_name', re: re_name, is_mask: false},
		{id: 'input_number_phone', re: re_phone, is_mask: true, mask: mask_phone},
		{id: 'input_passport_serial', re: re_passport_serial, is_mask: true, mask: mask_passport_serial},
		{id: 'input_passport_number', re: re_passport_number, is_mask: true, mask: mask_passport_number}
	]


// var mask = new IMask(document.getElementById(element_ids[3][0]), maskOptions);


function add_handler(){
	for (let i = element_ids.length - 1; i >= 0; i--) {
		let input = document.getElementById(element_ids[i].id);
		let re = element_ids[i].re;
		if (input) {
			input.addEventListener('focusout', ()=>{
				check_input(input, re)
			});
			if (element_ids[i].is_mask) {
				element_ids[i].imask = new IMask(input, element_ids[i].mask)
			}
		} else {
			console.log('Элемент не найден:', element_ids[i].id, '\nНомер:', i)
		}		
	}
}
add_handler()

function check_input(input, re) {
	console.log(input.id, '\n', input.value, re.test(input.value), '\n', re);
}

// AJAX пример
	// let xhr = new XMLHttpRequest();

	// xhr.open('GET', ip+'/api/check')
	// xhr.send()
	// xhr.onload = function() {
	//   alert(`Полученно: ${xhr.status} ${xhr.response}`);
	// };
	// xhr.onerror = function() { // происходит, только когда запрос совсем не получилось выполнить
	//   alert(`Ошибка соединения`);
	// };