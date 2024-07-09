import { useNotification } from "@kyvg/vue3-notification";
import axios from 'axios'

const { notify } = useNotification()



var mixin = {
  data() {
    return {
      // orderDetails: [],
      totalCount: 0,
      persianTotalCount: '',
      totalPrice: 0,
      persianTotalPrice: 0,
    };
  },
  methods: {

    toPersinaDigit(digit) {
      var id = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
      return digit.replace(/[0-9]/g, function (w) { return id[+w] });
    },
    BCupClick() {
      this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) + 1).toString())
    },
    BCdownClick() {
      if (parseInt(this.toEnglishDigit(this.number)) > 1)
        this.number = this.toPersinaDigit((parseInt(this.toEnglishDigit(this.number)) - 1).toString())
    },
    KeyUpFunction(k) {

      if ((k.key >= "0" && k.key <= "9") || k.key == "Backspace") {
        let en_number = this.number;

        let number = this.toEnglishDigit(en_number);
        let number_buffer = parseInt(number, 10);
        number = number_buffer.toString();
        // console.log(number)
        if (isNaN(number))
          number = "0";
        this.number = (this.toPersinaDigit(number));
      }
      else {
        this.number = (this.toPersinaDigit(parseInt(this.toEnglishDigit(this.number)).toString()));
      }
    },
    toEnglishDigit(replaceString) {
      var find = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
      var replace = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
      var regex;
      for (var i = 0; i < find.length; i++) {
        regex = new RegExp(find[i], "g");
        replaceString = replaceString.replace(regex, replace[i]);
      }
      return replaceString;
    },


  },

};


export default mixin