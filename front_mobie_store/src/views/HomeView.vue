<template>
  <div class="hero">
    <div class="glide" id="glide_1">
      <div class="glide__track" data-glide-el="track">
        <ul class="glide__slides">
          <sliderUpBox v-for="sliderUpp in sliderUp" v-bind:key="sliderUpp.id" v-bind:sliderUpp="sliderUpp" />
        </ul>
      </div>

      <div class="glide__bullets" data-glide-el="controls[nav]">
        <button class="glide__bullet" data-glide-dir="=0"></button>
        <button class="glide__bullet" data-glide-dir="=1"></button>
      </div>

      <div class="glide__arrows" data-glide-el="controls">
        <button class="glide__arrow glide__arrow--left" data-glide-dir="<">
          <img src="../assets/images/left-arrow-svgrepo-com.svg" alt="">
        </button>
        <button class="glide__arrow glide__arrow--right" data-glide-dir=">">
          <img src="../assets/images/right-arrow-svgrepo-com.svg" alt="">
        </button>
      </div>

    </div>
  </div>

  <main id="main">

    <section class="section collection" id="collection">
      <div class="container">
        <div class="collection__container">

          <div class="collection__box" v-for="sliderDown in sliderDowns" v-bind:key="sliderDown.id">
            <div class="img__container">
              <img :src="sliderDown.get_image_SliderDown" class="collection_02">
            </div>
            <div class="collection__content">
              <div class="collection__data">
                <span>{{ sliderDown.description1 }}</span>
                <h1>{{ sliderDown.title }}</h1>
                <a href="#">خرید</a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <div class="container">
      <section class="section latest__product" id="latest">
        <div class="title__container">
          <div class="section__title active" data-id="Latest Products">
            <span class="dot"></span>
            <h1 class="primary__title">آخرین محصولات</h1>
          </div>
        </div>

        <div class="container">
          <div class="glide" id="glide_2">
            <div class="glide__track" data-glide-el="track">
              <ul class="glide__slides latest-center">
                <ProductBox v-for="product in latestProduct" v-bind:key="product.id" v-bind:product="product" />
              </ul>
            </div>

            <div class="glide__arrows" data-glide-el="controls">
              <button class="glide__arrow glide__arrow--left" data-glide-dir="<">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                  version="1.1" id="Capa_1" width="800px" height="800px" viewBox="0 0 400.004 400.004"
                  xml:space="preserve">
                  <g>
                    <path
                      d="M382.688,182.686H59.116l77.209-77.214c6.764-6.76,6.764-17.726,0-24.485c-6.764-6.764-17.73-6.764-24.484,0L5.073,187.757   c-6.764,6.76-6.764,17.727,0,24.485l106.768,106.775c3.381,3.383,7.812,5.072,12.242,5.072c4.43,0,8.861-1.689,12.242-5.072   c6.764-6.76,6.764-17.726,0-24.484l-77.209-77.218h323.572c9.562,0,17.316-7.753,17.316-17.315   C400.004,190.438,392.251,182.686,382.688,182.686z" />
                  </g>
                </svg>
              </button>
              <button class="glide__arrow glide__arrow--right" data-glide-dir=">">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                  version="1.1" id="Capa_1" width="800px" height="800px" viewBox="0 0 400.004 400.004"
                  xml:space="preserve">
                  <g>
                    <path
                      d="M382.688,182.686H59.116l77.209-77.214c6.764-6.76,6.764-17.726,0-24.485c-6.764-6.764-17.73-6.764-24.484,0L5.073,187.757   c-6.764,6.76-6.764,17.727,0,24.485l106.768,106.775c3.381,3.383,7.812,5.072,12.242,5.072c4.43,0,8.861-1.689,12.242-5.072   c6.764-6.76,6.764-17.726,0-24.484l-77.209-77.218h323.572c9.562,0,17.316-7.753,17.316-17.315   C400.004,190.438,392.251,182.686,382.688,182.686z" />
                  </g>
                </svg>
              </button>
            </div>

          </div>
        </div>

      </section>

      <!-- Category Center -->
      <section class="category__section section" id="category">
        <div class="tab__list">
          <div class="title__container tabs">

            <div class="section__title ">

              <div class="section__title filter-btn" data-id="All Products" @click="getAllProducts()" :class="{
                'active': this.showMenu == 0,
              }">
                <span class="dot">
                </span>
                <h1 class="primary__title">محصولات</h1>
              </div>
            </div>

            <div class="section__title">
              <div class="section__title filter-btn" data-id="Trending Products" @click="getPopularProducts()" :class="{
                'active': this.showMenu == 1,
              }">
                <span class="dot">
                </span>
                <h1 class="primary__title">محصولات پرطرفدار</h1>
              </div>
            </div>


            <div class="section__title">
              <div class="section__title filter-btn" data-id="Featured Products" @click="getVigeProducts()" :class="{
                'active': this.showMenu == 2,
              }">
                <span class="dot">
                </span>
                <h1 class="primary__title">محصولات ویژه</h1>
              </div>
            </div>

            <div class="section__title">
              <div class="section__title filter-btn" data-id="Featured Products" @click="getPriceOffProducts()" :class="{
                'active': this.showMenu == 3,
              }">
                <span class="dot">
                </span>
                <h1 class="primary__title">تخفیف</h1>
              </div>
            </div>

          </div>

          <div class="category__container">
            <div class="category__center">

              <productListBox v-for="product1 in changeProduct" v-bind:key="product1.id" v-bind:product="product1" />


              <!-- 
              <div class="product"
              v-for="product in allProduct" 
              v-bind:key="product.id"
              >
                <div class="product__header">
                  <img :src="product.get_thumbnail"  alt="">
                </div>
                <div class="product__footer">
                  <h3>Apple iPhone 11</h3>
                  <div class="rating">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                      id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                      enable-background="new 0 0 122.88 116.864" xml:space="preserve">
                      <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                          points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0" />
                      </g>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                      id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                      enable-background="new 0 0 122.88 116.864" xml:space="preserve">
                      <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                          points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0" />
                      </g>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                      id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                      enable-background="new 0 0 122.88 116.864" xml:space="preserve">
                      <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                          points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0" />
                      </g>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                      id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                      enable-background="new 0 0 122.88 116.864" xml:space="preserve">
                      <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                          points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0" />
                      </g>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
                      id="Layer_1" x="0px" y="0px" width="122.88px" height="116.864px" viewBox="0 0 122.88 116.864"
                      enable-background="new 0 0 122.88 116.864" xml:space="preserve">
                      <g>
                        <polygon fill-rule="evenodd" clip-rule="evenodd"
                          points="61.44,0 78.351,41.326 122.88,44.638 88.803,73.491 99.412,116.864 61.44,93.371 23.468,116.864 34.078,73.491 0,44.638 44.529,41.326 61.44,0" />
                      </g>
                    </svg>
                  </div>

                  <div class="product__price">
                    <h4>$750</h4>
                    <a href="#"><button class="product__btn">ADD to Cart</button></a>
                  </div>

                  <ul>

                    <a href="#" data>
                      
                      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                        version="1.1" id="Capa_1" width="800px" height="800px" viewBox="0 0 442.04 442.04"
                        xml:space="preserve">
                        <g>
                          <g>
                            <path
                              d="M221.02,341.304c-49.708,0-103.206-19.44-154.71-56.22C27.808,257.59,4.044,230.351,3.051,229.203    c-4.068-4.697-4.068-11.669,0-16.367c0.993-1.146,24.756-28.387,63.259-55.881c51.505-36.777,105.003-56.219,154.71-56.219    c49.708,0,103.207,19.441,154.71,56.219c38.502,27.494,62.266,54.734,63.259,55.881c4.068,4.697,4.068,11.669,0,16.367    c-0.993,1.146-24.756,28.387-63.259,55.881C324.227,321.863,270.729,341.304,221.02,341.304z M29.638,221.021    c9.61,9.799,27.747,27.03,51.694,44.071c32.83,23.361,83.714,51.212,139.688,51.212s106.859-27.851,139.688-51.212    c23.944-17.038,42.082-34.271,51.694-44.071c-9.609-9.799-27.747-27.03-51.694-44.071    c-32.829-23.362-83.714-51.212-139.688-51.212s-106.858,27.85-139.688,51.212C57.388,193.988,39.25,211.219,29.638,221.021z" />
                          </g>
                          <g>
                            <path
                              d="M221.02,298.521c-42.734,0-77.5-34.767-77.5-77.5c0-42.733,34.766-77.5,77.5-77.5c18.794,0,36.924,6.814,51.048,19.188    c5.193,4.549,5.715,12.446,1.166,17.639c-4.549,5.193-12.447,5.714-17.639,1.166c-9.564-8.379-21.844-12.993-34.576-12.993    c-28.949,0-52.5,23.552-52.5,52.5s23.551,52.5,52.5,52.5c28.95,0,52.5-23.552,52.5-52.5c0-6.903,5.597-12.5,12.5-12.5    s12.5,5.597,12.5,12.5C298.521,263.754,263.754,298.521,221.02,298.521z" />
                          </g>
                          <g>
                            <path
                              d="M221.02,246.021c-13.785,0-25-11.215-25-25s11.215-25,25-25c13.786,0,25,11.215,25,25S234.806,246.021,221.02,246.021z" />
                          </g>
                        </g>
                      </svg> </a>
                    <a href="#" data>
                      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"
                        height="800px" width="800px" version="1.1" id="Capa_1" viewBox="0 0 471.701 471.701"
                        xml:space="preserve">
                        <g>
                          <path
                            d="M433.601,67.001c-24.7-24.7-57.4-38.2-92.3-38.2s-67.7,13.6-92.4,38.3l-12.9,12.9l-13.1-13.1   c-24.7-24.7-57.6-38.4-92.5-38.4c-34.8,0-67.6,13.6-92.2,38.2c-24.7,24.7-38.3,57.5-38.2,92.4c0,34.9,13.7,67.6,38.4,92.3   l187.8,187.8c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-3.9l188.2-187.5c24.7-24.7,38.3-57.5,38.3-92.4   C471.801,124.501,458.301,91.701,433.601,67.001z M414.401,232.701l-178.7,178l-178.3-178.3c-19.6-19.6-30.4-45.6-30.4-73.3   s10.7-53.7,30.3-73.2c19.5-19.5,45.5-30.3,73.1-30.3c27.7,0,53.8,10.8,73.4,30.4l22.6,22.6c5.3,5.3,13.8,5.3,19.1,0l22.4-22.4   c19.6-19.6,45.7-30.4,73.3-30.4c27.6,0,53.6,10.8,73.2,30.3c19.6,19.6,30.3,45.6,30.3,73.3   C444.801,187.101,434.001,213.101,414.401,232.701z" />
                        </g>
                      </svg>
                    </a>
                    <a href="#" data>
                      <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 16 16">
                        <path fill="currentColor"
                          d="M13.901 2.599A8 8 0 0 0 0 8h1.5a6.5 6.5 0 0 1 11.339-4.339L10.5 6H16V.5l-2.099 2.099zM14.5 8a6.5 6.5 0 0 1-11.339 4.339L5.5 10H0v5.5l2.099-2.099A8 8 0 0 0 16 8h-1.5z" />
                      </svg>
                    </a>

                  </ul>
                </div>

              </div> -->

            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- Facility section -->
    <!--

      <section class="facility__section section" id="factility">
        <div class="container">
          <div class="factility__container">
  
            <div class="factility__box">
              <div class="factility-img__container">
                <svg class="svg-icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M618.771648 341.718335l25.103501 0c21.260294 0 31.931326-9.07651 31.931326-27.433956 0-20.810557-19.778206-31.266941-59.344839-31.266941l-41.375802 0-62.605432-83.323997 29.570207 0c19.778206 0 29.672419-9.178723 29.672419-27.352186 0-20.974097-13.757863-31.348712-41.365581-31.348712l-60.397632 0C400.219918 47.028178 356.27857 0 337.941567 0c-8.504117 0-17.723726 3.465019-27.62816 10.405278-9.914656 6.86871-14.800435 14.268928-14.800435 22.057555 0 7.849955 10.49727 28.077897 31.532695 60.714492 20.99454 32.59571 51.668646 93.586177 91.725902 182.848747 40.108362 89.272791 60.131879 143.292335 60.131879 161.895092 0 11.938473-17.887266 18.520987-53.764012 19.65555-117.718655 0.715491-202.146552 6.275875-253.263248 16.681153-5.969236-5.182197-20.606131-24.122256-43.88002-56.717966-23.335217-32.59571-39.372428-52.057056-48.101414-58.138726-8.810756-6.132777-24.30624-9.240051-46.680654-9.240051-11.938473 0-19.982632 1.706956-24.07115 5.059541 0 14.463132 17.641955 66.898376 53.079185 157.111526C26.795125 594.378527 9.15317 646.711558 9.15317 669.474382c4.088518 3.332142 12.132677 5.028877 24.07115 5.028877 22.364194 0 37.767685-2.964176 46.363794-8.984518 8.626773-5.928351 24.663985-25.297705 48.121857-58.138726 23.478315-32.789914 38.207201-51.791302 44.176437-57.004162 51.106475 9.301378 110.165118 14.28937 177.574559 15.025304 67.215236 0.86881 105.739297 2.749528 115.183774 5.938572 9.536468 3.199265 14.279149 8.28947 14.279149 15.331943 0 18.316561-20.023517 72.131679-60.131879 161.619117-40.057255 89.528323-70.731362 150.580118-91.725902 183.145164-21.045646 32.697923-31.532695 52.895202-31.532695 60.765599 0 7.788627 4.885779 15.055968 14.800435 21.750916 9.894214 6.725612 19.124043 10.108861 27.62816 10.108861 18.337003 0 62.278351-46.833974 132.028468-140.399709l60.397632 0c27.607718 0 41.365581-10.435942 41.365581-31.318048 0-18.337003-9.904435-27.413513-29.672419-27.413513l-29.570207 0 62.605432-83.272891 41.375802 0c39.566633 0 59.344839-10.476827 59.344839-31.287384 0-18.367667-10.671032-27.485062-31.931326-27.485062l-25.103501 0 99.514528-117.99463 129.800226 0c110.635297 0 166.004053-18.459659 166.004053-55.358534 0-14.534682-22.272202-26.503818-66.888155-35.815418-44.483076-9.219608-77.538744-13.921404-99.115898-13.921404L718.296398 459.794736 618.771648 341.718335z" />
                </svg>
              </div>
              <p>خرید رایگان</p>
            </div>
  
            <div class="factility__box">
              <div class="factility-img__container">
                <svg id="credit-card" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20.27 13.504">
                  <path id="Path_600" data-name="Path 600"
                    d="M0,213.143v5.246a2.735,2.735,0,0,0,2.735,2.735h14.8a2.735,2.735,0,0,0,2.735-2.735v-5.246a.476.476,0,0,0-.476-.476H.476A.476.476,0,0,0,0,213.143Zm5.061,3.33H3.792a.832.832,0,1,1,0-1.665H5.061a.832.832,0,1,1,0,1.665Z"
                    transform="translate(0 -207.619)" />
                  <path id="Path_601" data-name="Path 601"
                    d="M20.27,88.241v-.172a2.735,2.735,0,0,0-2.735-2.735H2.735A2.735,2.735,0,0,0,0,88.069v.172a.476.476,0,0,0,.476.476H19.794A.476.476,0,0,0,20.27,88.241Z"
                    transform="translate(0 -85.334)" />
                </svg>
              </div>
              <p>۱۰۰% ضمانت برگشت پول</p>
            </div>
  
            <div class="factility__box">
              <div class="factility-img__container">
                <svg width="800px" height="800px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M6 15H8M3 11H21M3 8H21M12 15H16M6.2 19H17.8C18.9201 19 19.4802 19 19.908 18.782C20.2843 18.5903 20.5903 18.2843 20.782 17.908C21 17.4802 21 16.9201 21 15.8V8.2C21 7.0799 21 6.51984 20.782 6.09202C20.5903 5.71569 20.2843 5.40973 19.908 5.21799C19.4802 5 18.9201 5 17.8 5H6.2C5.0799 5 4.51984 5 4.09202 5.21799C3.71569 5.40973 3.40973 5.71569 3.21799 6.09202C3 6.51984 3 7.07989 3 8.2V15.8C3 16.9201 3 17.4802 3.21799 17.908C3.40973 18.2843 3.71569 18.5903 4.09202 18.782C4.51984 19 5.07989 19 6.2 19Z"
                    stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
              </div>
              <p>درگاه پرداخت متعدد</p>
            </div>
  
            <div class="factility__box">
              <div class="factility-img__container">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
                  <rect width="256" height="256" fill="none" />
                  <path
                    d="M224,136H192a16,16,0,0,0-16,16v40a16,16,0,0,0,16,16h16a16,16,0,0,0,16-16V136a96,96,0,1,0-192,0v56a16,16,0,0,0,16,16H64a16,16,0,0,0,16-16V152a16,16,0,0,0-16-16H32"
                    fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="16" />
                </svg>
              </div>
              <p>پشتیبانی آنلاین</p>
            </div>
  
  
          </div>
        </div>
      </section>
    -->

    <!-- Testimonial -->
    <section class="section testimonial" id="testimonial">
      <div class="testimonial__container">


        <div class="glide" id="glide_3">
          <div class="glide__track" data-glide-el="track">
            <ul class="glide__slides">

              <li class="glide__slide" v-for="founderData in foundersData" v-bind:key="founderData.id">
                <div class="testimonial__box">
                  <div class="client__image">
                    <img :src="founderData.get_image" alt="">
                  </div>
                  <p>{{ founderData.description }}</p>
                  <div class="client__info">
                    <h3>{{ founderData.title }}</h3>
                    <span>{{ founderData.position }}</span>
                  </div>
                </div>
              </li>

              <!-- <li class="glide__slide">
                <div class="testimonial__box">
                  <div class="client__image">
                    <img src="../assets/images/profile2.jpg" alt="">
                  </div>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto tenetur similique sint quos
                    officiis minus, hic laboriosam saepe libero sapiente beatae vel! Adipisci architecto sapiente alias
                    eos quis, animi culpa!</p>
                  <div class="client__info">
                    <h3>john Smith</h3>
                    <span>Founder at APPLE</span>
                  </div>
                </div>
              </li>

              <li class="glide__slide">
                <div class="testimonial__box">
                  <div class="client__image">
                    <img src="../assets/images/profile3.jpg" alt="">
                  </div>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto tenetur similique sint quos
                    officiis minus, hic laboriosam saepe libero sapiente beatae vel! Adipisci architecto sapiente alias
                    eos quis, animi culpa!</p>
                  <div class="client__info">
                    <h3>john Smith</h3>
                    <span>Founder at APPLE</span>
                  </div>
                </div>
              </li> -->

              <!-- <li class="glide__slide">
                <div class="testimonial__box">
                  <div class="client__image">
                    <img src="../assets/images/profile4.jpg" alt="">
                  </div>
                  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto tenetur similique sint quos
                    officiis minus, hic laboriosam saepe libero sapiente beatae vel! Adipisci architecto sapiente alias
                    eos quis, animi culpa!</p>
                  <div class="client__info">
                    <h3>john Smith</h3>
                    <span>Founder at APPLE</span>
                  </div>
                </div>
              </li> -->

            </ul>
          </div>

          <div class="glide__bullets" data-glide-el="controls[nav]">
            <button class="glide__bullet" data-glide-dir="=0"></button>
            <button class="glide__bullet" data-glide-dir="=1"></button>
            <button class="glide__bullet" data-glide-dir="=2"></button>
          </div>
        </div>

      </div>
    </section>

    <!-- New Section -->
    <!-- <section class="section news" id="news">
      <div class="container">
        <div class="title__container">
          <div class="section__titles">
            <div class="section__title active">
              <span class="dot"></span>
              <h1 class="primary__title">اخبار</h1>
            </div>
          </div>
        </div>
      </div>

      <div class="news__container">
        <div class="glide" id="glide_4">
          <div class="glide__track" data-glide-el="track">
            <ul class="glide__slides">

              <li class="glide__slide">
                <div class="new__card">
                  <div class="card__header">
                    <img src="../assets/images/news1.jpg" alt="">
                  </div>
                  <div class="card__footer">
                    <h3>Styling White Shirts After A Cool Day</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, nisi! Quisquam excepturi asperiores, in vel molestiae alias veritatis quasi voluptatibus possimus qui laboriosam, sit dolor accusamus magnam eos. Incidunt, illum.</p>
                    <a href="#">Read More</a>
                  </div>
                </div>
              </li>

              <li class="glide__slide">
                <div class="new__card">
                  <div class="card__header">
                    <img src="../assets/images/news2.jpg" alt="">
                  </div>
                  <div class="card__footer">
                    <h3>Styling White Shirts After A Cool Day</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, nisi! Quisquam excepturi asperiores, in vel molestiae alias veritatis quasi voluptatibus possimus qui laboriosam, sit dolor accusamus magnam eos. Incidunt, illum.</p>
                    <a href="#">Read More</a>
                  </div>
                </div>
              </li>

              <li class="glide__slide">
                <div class="new__card">
                  <div class="card__header">
                    <img src="../assets/images/news3.jpg" alt="">
                  </div>
                  <div class="card__footer">
                    <h3>Styling White Shirts After A Cool Day</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, nisi! Quisquam excepturi asperiores, in vel molestiae alias veritatis quasi voluptatibus possimus qui laboriosam, sit dolor accusamus magnam eos. Incidunt, illum.</p>
                    <a href="#">Read More</a>
                  </div>
                </div>
              </li>

              <li class="glide__slide">
                <div class="new__card">
                  <div class="card__header">
                    <img src="../assets/images/news4.jpg" alt="">
                  </div>
                  <div class="card__footer">
                    <h3>Styling White Shirts After A Cool Day</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, nisi! Quisquam excepturi asperiores, in vel molestiae alias veritatis quasi voluptatibus possimus qui laboriosam, sit dolor accusamus magnam eos. Incidunt, illum.</p>
                    <a href="#">Read More</a>
                  </div>
                </div>
              </li>

              <li class="glide__slide">
                <div class="new__card">
                  <div class="card__header">
                    <img src="../assets/images/news5.jpg" alt="">
                  </div>
                  <div class="card__footer">
                    <h3>Styling White Shirts After A Cool Day</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, nisi! Quisquam excepturi asperiores, in vel molestiae alias veritatis quasi voluptatibus possimus qui laboriosam, sit dolor accusamus magnam eos. Incidunt, illum.</p>
                    <a href="#">Read More</a>
                  </div>
                </div>
              </li>


            </ul>
          </div>
        </div>
      </div>
    </section> -->

    <!-- NewsLetters -->
    <!-- <section class="section newsletter" id="contact">
      <div class="container">
        <div class="newsletter__content">
          <div class="newsletter__data">
            <h3>اشتراک در خبرنامه</h3>
            <p>جمله‌ای گزاف که توصیف می‌کند چه چیزی با مشترک شدن دریافت می‌کند</p>
          </div>
          <form action="#">
            <input type="email" class="newsletter__email" placeholder="ایمیل خود را وارد کنید">
            <a href="#" class="newsletter__link">اشتراک</a>
          </form>
        </div>
      </div>
    </section> -->
  </main>
</template>

<script>

import Glide from '@glidejs/glide'
import '@glidejs/glide/dist/css/glide.core.min.css'
import '@glidejs/glide/dist/css/glide.theme.min.css'

import axios from 'axios';
import ProductBox from '@/components/productBox.vue'
import sliderUpBox from '@/components/sliderUpBox.vue'
import productListBox from '@/components/productListBox.vue'

import { Autoplay } from '@glidejs/glide/dist/glide.modular.esm'

export default {
  name: 'HomeView',
  data() {
    return {
      showMenu: 0,
      latestProduct: [],
      changeProduct: [],
      sliderUp: [],
      sliderDowns: [],
      foundersData: [],
      glide1: "",
      glide2: "",
      query: '',
      state: '',
      code: '',
    }
  },
  components: {
    ProductBox,
    sliderUpBox,
    productListBox,
  },
  mounted() {
    document.title = 'خانه' + ' | موبایل'
    this.getLatestProducts()
    this.getAllProducts()

    this.getSliderUp()
    this.getSliderDown()
    this.getFounders()
    window.scroll(0, 0);

/*
let uri = window.location.href.split('?');

console.log(uri)
if (uri.length == 2) {
  let vars = uri[1].split('&');
  let getVars = {};
  let tmp = '';
  vars.forEach(function (v) {
    tmp = v.split('=');
    if (tmp.length == 2)
      getVars[tmp[0]] = tmp[1];
  });
  // console.log(getVars);

  // console.log(getVars['state'])
  // console.log(getVars['code'])

  this.state = getVars['state']
  this.code = getVars['code']

  console.log(this.state)
  console.log(this.code)
  console.log(`${axios.defaults.baseURL}api/v1/o/google-oauth2/?state=${this.state}&code=${this.code}`)
  if (this.state && this.code) {
    console.log("kir khordi")
  }
  // axios.post(`api/v1/o/google-oauth2/?state=${state}&code=${code}`)
  // .then(response => {
  //     console.log("++++++++++++++++++++++++")
  //     console.log(response)
  // })
}
this.googleLogin()
 */
    // let uri = window.location.search.substring(1)
    // let params = new URLSearchParams(uri)
    // if (params.get('state') && params.get('code')) {
    //   const state = params.get('state')
    //   const code = params.get('code')
    //   console.log(uri)
    //   console.log(state)
    //   console.log(typeof(params.get('code')),code)
    //   console.log("4%2F0AfJohXk")

    //   // axios.post(`/api/v1/o/google-oauth2/?state=${state}&code=${code}`)
    //   // .then(response => {
    //   //     console.log("++++++++++++++++++++++++")
    //   //     console.log(response)
    //   // })
    // }
    // else{
    //   console.log("kir khordi")
    //   console.log("%2F0A")
    // }

  },
  methods: {
    async getLatestProducts() {
      await axios
        .get('/api/v1/latest-product/')
        .then(response => {
          this.latestProduct = response.data
        })
    },
    async googleLogin() {
      // await axios.post(`/api/v1/o/google-oauth2/?state=${this.state}&code=${this.code}`, {})
      // await axios.post("http://127.0.0.1:8000/api/v1/o/google-oauth2/?state=mgPdQffepPVZ10KRuwx0NhWZPlhOv76F&code=4%2F0AfJohXm6ZFfcaC191qpDlB_cKa9p16oUif1xOZhhdLqUW973y8JK5HGIhojQWQvnu_TiJA")
      //   .then((response) => {
      //     // console.log("++++++++++++++++++++++++")
      //     // console.log(response)
      //     // console.log(response.data)
      //     alert (response.data)
      //   })
      //   .catch((error) => {
      //     console.log(error.response)
      //     // this.errors.push(error.response)
      //     for (const property in error.response.data) {
      //       console.log(`${error.response.data[property]}`)
      //     }
      //   });
      await fetch("http://127.0.0.1:8000/api/v1/o/google-oauth2/?state=mgPdQffepPVZ10KRuwx0NhWZPlhOv76F&code=4%2F0AfJohXm6ZFfcaC191qpDlB_cKa9p16oUif1xOZhhdLqUW973y8JK5HGIhojQWQvnu_TiJA", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        // body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(response => console.log(JSON.stringify(response)))
      // .then(res => {
      //   console.log("Request complete! response:", res.body);
      // });
    },
    async getAllProducts() {
      // this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/all-product/')
        .then(response => {
          this.changeProduct = response.data
          this.showMenu = 0
        })
        // this.$store.commit('setIsLoading', false)
    },

    async getPopularProducts() {
      await axios
        .get('/api/v1/PopularProductsList/')
        .then(response => {
          this.changeProduct = response.data
          this.showMenu = 1
        })
    },

    async getVigeProducts() {
      await axios
        .get('/api/v1/vigeProductsList/')
        .then(response => {
          this.changeProduct = response.data
          this.showMenu = 2
        })
    },
    async getPriceOffProducts() {
      await axios
        .get('/api/v1/priceOffList/')
        .then(response => {
          this.changeProduct = response.data
          this.showMenu = 3
        })
    },

    async getSliderUp() {
      await axios
        .get('/slider/sliderUp/')
        .then(response => {
          this.sliderUp = response.data
          // this.glide1.update({ autoplay: 3000 });
          // this.glide1.mount();
        })
    },
    //
    async getSliderDown() {
      await axios
        .get('/slider/sliderDown/')
        .then(response => {
          this.sliderDowns = response.data
        })
    },

    async getFounders() {
      await axios
        .get('/founders/')
        .then(response => {
          this.foundersData = response.data
          // console.log(this.foundersData)
        })
    },
  },
  updated() {
    /*
    ==========================
    Glide Js Carsousel
    ==========================
    */


    const slider1 = document.getElementById('glide_1');
    /*
    ==========================
    Hero
    ==========================
    */

    if (slider1) {
      this.glide1 = new Glide(slider1, {
        type: 'carsoual',
        startAt: 0,
        hoverpause: true,
        perView: 1,
        animationDuration: 800,
        animationTimingFunc: 'linear',
        // autoplay: 3000,
      });
    }
    // this.glide1.pause();
    // this.glide1.pause();
    // glide.play(4000)
    this.glide1.mount();
    // this.glide1.destroy();
    // this.glide1.disable();
    // this.glide1.update({ autoplay: 3000 });
    // glide.go('>')
    // this.glide1.on('mount.after', function () {
    //   this.glide1.update({ autoplay: 3000 });
    //   console.log("kir khar");
    // })





    const slider2 = document.getElementById('glide_2');
    if (slider2) {
      this.glide2 = new Glide(slider2, {
        type: 'carsoual',
        startAt: 0,
        hoverpause: true,
        perView: 4,
        animationDuration: 800,
        animationTimingFunc: "ease-in-out",
        breakpoints: {
          1200: {
            perView: 3,
          },
          768: {
            perView: 2,
          },
        },
      }).mount();
    }

    const slider3 = document.getElementById('glide_3');

    // const slider4 = document.getElementById('glide_4');


    if (slider3) {
      new Glide(slider3, {
        type: 'carsoual',
        startAt: 0,
        hoverpause: true,
        perView: 1,
        animationDuration: 800,
        animationTimingFunc: "ease-in-out",
      }).mount();
    }

    // if (slider4) {
    //   new Glide(slider4, {
    //     type: 'carsoual',
    //     startAt: 0,
    //     hoverpause: true,
    //     autoplay: 3000,
    //     perView: 3,
    //     animationDuration: 800,
    //     animationTimingFunc: "ease-in-out",
    //     breakpoints:{
    //       998:{
    //         perView: 2,
    //       },
    //       768:{
    //          perView: 1,
    //       }
    //     },
    //   }).mount();
    // }
  },
}
</script>
