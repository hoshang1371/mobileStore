import {ref} from 'vue'
export default function useComp(){

    // const reuseData = ref ("Reusable data")
    // function reuseMethod(hhhh) {
    //     console.log(hhhh);
    //     console.log('Hello from Reusable method!')
    //     return hhhh
    // }
    function toPersinaDigit(digit) {
          var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
          return digit.replace(/[0-9]/g, function (w) { return id[+w] });
    }
    return {
        // reuseData,
        // reuseMethod,
        toPersinaDigit
    }
}