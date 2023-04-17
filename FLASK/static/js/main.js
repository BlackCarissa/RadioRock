// возвращает куки с указанным name,
// или undefined, если ничего не найдено
function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    console.log(matches)
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }

  function setCookie(name, value, options = {}) {

    options = {
      path: '/',
      // при необходимости добавьте другие значения по умолчанию
      ...options
    };
  
    if (options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }
  
    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  
    for (let optionKey in options) {
      updatedCookie += "; " + optionKey;
      let optionValue = options[optionKey];
      if (optionValue !== true) {
        updatedCookie += "=" + optionValue;
      }
    }
  
    document.cookie = updatedCookie;
  }

const cookieAlert = document.querySelector(".cookie-alert--js")
const cookieAlert_btn = document.querySelector(".cookie-alert__btn--js")
if ((getCookie('visit'))!=true) {
  console.log('КУКИИИИ')
  setTimeout(()=>{
    cookieAlert.classList.add('is-show')},1000)
  cookieAlert_btn.addEventListener('click',()=>{
    cookieAlert.classList.remove('is-show')
    setCookie('visit',true)
    })
}
