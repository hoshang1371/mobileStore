const mixin= {
    data() {
      return {
        orderDetails: [],
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

    },

  };


export default mixin