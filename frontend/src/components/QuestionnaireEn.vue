<template>
    <v-app>
        <v-expansion-panels
                v-model='active_question'
                focusable
                hover
        >
            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你购买电脑的预算最接近以下哪个数字？
                    <template v-slot:actions>
                        <!--                        <v-icon v-if="is_finish[0] === 0" color="error">mdi-alert-circle</v-icon>-->
                        <v-icon v-if="price === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="price !== ''" color="teal">mdi-check</v-icon>
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="price" column>
                        <v-radio
                                label="¥ 4000"
                                color="orange darken-3"
                                value='4000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 5000"
                                color="orange darken-3"
                                value='5000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 6000"
                                color="orange darken-3"
                                value='6000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 7000"
                                color="orange darken-3"
                                value='7000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 8000"
                                color="orange darken-3"
                                value='8000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 9000"
                                color="orange darken-3"
                                value='9000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ 10000"
                                color="orange darken-3"
                                value='10000'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="¥ >10000"
                                color="orange darken-3"
                                value='11000'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你是否只想要苹果电脑（MacBook）？
                    <template v-slot:actions>
                        <v-icon v-if="brand.length === 0" color="primary">$expand</v-icon>
                        <v-icon v-else-if="brand.length !== 0" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="brand" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='apple'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='none'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你选购的电脑主要出于以下什么用途？
                    <template v-slot:actions>
                        <v-icon v-if="purpose === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="purpose !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="purpose" column>
                        <v-radio
                                label="只是用来看视频或者浏览网页，或者使用一些简单的软件，如OFFICE三件套"
                                color="orange darken-3"
                                value='video'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="工作，例如经常使用三维建模软件或视频剪辑软件等，如LIG，SOLIDWORKS"
                                color="orange darken-3"
                                value='work'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="学习，并且游玩一些比较基础的网游，如英雄联盟"
                                color="orange darken-3"
                                value='study'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="除了上述，还经常玩游戏，并且对游戏画质有较高的要求"
                                color="orange darken-3"
                                value='game'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    你是否对酷炫的彩色RGB灯带键盘有所追求？(RGB灯带可开可关)
                    <template v-slot:actions>
                        <v-icon v-if="rgb_require === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="rgb_require !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="rgb_require" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='true'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='false'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问您是否经常会携带你的电脑外出？
                    <template v-slot:actions>
                        <v-icon v-if="bringout === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="bringout !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="bringout" column>
                        <v-radio
                                label="是"
                                color="orange darken-3"
                                value='yes'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="不是"
                                color="orange darken-3"
                                value='no'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <v-expansion-panel-header disable-icon-rotate>
                    请问你对屏幕大小和重量更满足以下哪一类？
                    <template v-slot:actions>
                        <v-icon v-if="screen === ''" color="primary">$expand</v-icon>
                        <v-icon v-else-if="screen !== ''" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    <v-radio-group
                            v-model="screen" column>
                        <v-radio
                                label="我要大，重不重无所谓"
                                color="orange darken-3"
                                value='big'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="中等，15.3寸就很标准"
                                color="orange darken-3"
                                value='medium'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="小一些，我喜欢小巧轻便的"
                                color="orange darken-3"
                                value='small'
                                v-on:click="jump"
                        ></v-radio>
                        <v-radio
                                label="无所谓"
                                color="orange darken-3"
                                value='dontcare'
                                v-on:click="jump"
                        ></v-radio>
                    </v-radio-group>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <v-expansion-panel>
                <div v-if="purpose === 'game'">
                    <v-expansion-panel-header disable-icon-rotate>
                        您是否对每年新出的3A大作非常感兴趣，期待特效全开，尽兴畅玩？
                        <template v-slot:actions>
                            <v-icon v-if="game_3A === ''" color="primary">$expand</v-icon>
                            <v-icon v-else-if="game_3A !== ''" color="teal">mdi-check</v-icon>
                            <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <v-radio-group
                                v-model="game_3A" column>
                            <v-radio
                                    label="是"
                                    color="orange darken-3"
                                    value='3A'
                                    v-on:click="jump"
                            ></v-radio>
                            <v-radio
                                    label="不是"
                                    color="orange darken-3"
                                    value='no'
                                    v-on:click="jump"
                            ></v-radio>
                        </v-radio-group>
                    </v-expansion-panel-content>
                </div>

                <div v-else-if="purpose === 'work'">
                    <v-expansion-panel-header disable-icon-rotate>
                        您在工作中对电脑的使用更符合以下哪种描述？
                        <template v-slot:actions>
                            <v-icon v-if="software === ''" color="primary">$expand</v-icon>
                            <v-icon v-else-if="software !== ''" color="teal">mdi-check</v-icon>
                            <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <v-radio-group
                                v-model="software" column>
                            <v-radio
                                    label="使用以下简单的软件如:OFFICE 三件套，编程软件，数据处理，统计软件（SPSS,MATLAB,STATA），二维制图软件（平面CAO），平面设计软件（PS，AI）等"
                                    color="orange darken-3"
                                    value='2D'
                                    v-on:click="jump"
                            ></v-radio>
                            <v-radio
                                    label="经常使用三维建模软件:如LIG,3DMAS,CAO(3D),PROE,BIM,CIATA,SOLIDWORKS等，或经常使用视频剪辑软件如：PR,AE,VEGAS等"
                                    color="orange darken-3"
                                    value='3D'
                                    v-on:click="jump"
                            ></v-radio>
                            <v-radio
                                    label="程序猿大佬，经常使用计算机进行大量数据运算和训练复杂的神经网络"
                                    color="orange darken-3"
                                    value='DP'
                                    v-on:click="jump"
                            ></v-radio>
                        </v-radio-group>
                    </v-expansion-panel-content>
                </div>

                <div v-else-if="purpose === 'study'">
                    <v-expansion-panel-header disable-icon-rotate>
                        请问你学习中对电脑的使用最接近于如下哪一类？
                        <template v-slot:actions>
                            <v-icon v-if="study_purpose === ''" color="primary">$expand</v-icon>
                            <v-icon v-else-if="study_purpose !== ''" color="teal">mdi-check</v-icon>
                            <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                        </template>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                        <v-radio-group
                                v-model="study_purpose" column>
                            <v-radio
                                    label="主要是用来阅读文献和写作"
                                    color="orange darken-3"
                                    value='reading'
                                    v-on:click="jump"
                            ></v-radio>
                            <v-radio
                                    label="会用来做各种软件仿真和代码编写"
                                    color="orange darken-3"
                                    value='coding'
                                    v-on:click="jump"
                            ></v-radio>
                            <v-radio
                                    label="我也许会用它来处理大量的数据和训练较为复杂的神经网络"
                                    color="orange darken-3"
                                    value='deeplearning'
                                    v-on:click="jump"
                            ></v-radio>
                        </v-radio-group>
                    </v-expansion-panel-content>
                </div>
            </v-expansion-panel>


            <v-expansion-panel v-if="flag_addq2 == true">
                <v-expansion-panel-header disable-icon-rotate>
                    以下是2020年对笔记本品牌效应的评估，请选择一个你非常喜欢的品牌。
                    <template v-slot:actions>
                        <v-icon v-if="brand === 'none'" color="primary">$expand</v-icon>
                        <v-icon v-else-if="brand !== 'none'" color="teal">mdi-check</v-icon>
                        <!--                        <v-icon v-else color="error">mdi-alert-circle</v-icon>-->
                    </template>
                </v-expansion-panel-header>
                <v-expansion-panel-content class="text-left">
                    一线品牌<br>
                    具有对笔记本模具的设计能力和拥有自己的代工厂，售后网点全国铺开。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="first_brand in first_brands.slice(0,5)"
                                        :key="first_brand"
                                        multiple

                                        color="primary"
                                        v-model="brand"
                                        :label="first_brand"
                                        :value="first_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="first_brand in first_brands.slice(5,10)"
                                        :key="first_brand"
                                        multiple

                                        color="primary"
                                        v-model="brand"
                                        :label="first_brand"
                                        :value="first_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="first_brand in first_brands.slice(10,15)"
                                        :key="first_brand"
                                        multiple

                                        color="primary"
                                        v-model="brand"
                                        :label="first_brand"
                                        :value="first_brand"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>

                    二线品牌<br>
                    贴牌其他厂家的产品进行销售。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="second_brand in second_brands.slice(0,4)"
                                        :key="second_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="second_brand"
                                        :value="second_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="second_brand in second_brands.slice(4,8)"
                                        :key="second_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="second_brand"
                                        :value="second_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="second_brand in second_brands.slice(8,12)"
                                        :key="second_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="second_brand"
                                        :value="second_brand"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>

                    三线品牌<br>
                    以较低的价格提供较高的配置。
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="third_brand in third_brands.slice(0,3)"
                                        :key="third_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="third_brand"
                                        :value="third_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="third_brand in third_brands.slice(3,6)"
                                        :key="third_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="third_brand"
                                        :value="third_brand"
                                >
                                </v-checkbox>
                            </v-col>
                            <v-col cols="12" sm="4" md="4">
                                <v-checkbox
                                        v-for="third_brand in third_brands.slice(6,9)"
                                        :key="third_brand"
                                        multiple
                                        color="primary"
                                        v-model="brand"
                                        :label="third_brand"
                                        :value="third_brand"
                                >
                                </v-checkbox>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-expansion-panel-content>
            </v-expansion-panel>


            <!--            <v-expansion-panel>-->
            <!--                <v-expansion-panel-header disable-icon-rotate>-->
            <!--                    4. 你最常使用电脑的时间段是？-->
            <!--                    <template v-slot:actions>-->
            <!--                        <v-icon v-if="use_time === ''" color="primary">$expand</v-icon>-->
            <!--                        <v-icon v-else-if="use_time !== ''" color="teal">mdi-check</v-icon>-->
            <!--                        &lt;!&ndash;                        <v-icon v-else color="error">mdi-alert-circle</v-icon>&ndash;&gt;-->
            <!--                    </template>-->
            <!--                </v-expansion-panel-header>-->
            <!--                <v-expansion-panel-content>-->
            <!--                    <v-radio-group-->
            <!--                            v-model="use_time" column>-->
            <!--                        <v-radio-->
            <!--                                label="只有上午或下午"-->
            <!--                                color="orange darken-3"-->
            <!--                                value='morning'-->
            <!--                                v-on:click="jump"-->
            <!--                        ></v-radio>-->
            <!--                        <v-radio-->
            <!--                                label="晚上"-->
            <!--                                color="orange darken-3"-->
            <!--                                value='evening'-->
            <!--                                v-on:click="jump"-->
            <!--                        ></v-radio>-->
            <!--                        <v-radio-->
            <!--                                label="整天(这一项有错误，不能选)"-->
            <!--                                color="orange darken-3"-->
            <!--                                value='allday'-->
            <!--                                v-on:click="jump"-->
            <!--                        ></v-radio>-->
            <!--                    </v-radio-group>-->
            <!--                </v-expansion-panel-content>-->
            <!--            </v-expansion-panel>-->


        </v-expansion-panels>


        <div>
            <v-btn
                    rounded
                    class="ma-2"
                    color="primary"
                    dark
                    v-on:click="submit"
            >提交
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>
        </div>

        <!--进度条组件-->
        <v-progress-linear
                fixed
                background-opacity="0.3"
                :value="degree"
                color="primary"
        ></v-progress-linear>


        <!--浮动按钮-->
        <v-speed-dial
                v-model="fab"
                fixed
                bottom
                left
                direction="top"
                transition="slide-y-reverse-transition"

        >
            <template v-slot:activator>
                <v-btn
                        v-model="fab"
                        color="blue darken-2"
                        dark
                        fab
                >
                    <v-icon v-if="fab">mdi-close</v-icon>
                    <v-icon v-else>mdi-menu</v-icon>
                </v-btn>
            </template>
            <v-btn
                    fab
                    dark
                    small
                    color="green"
            >
                En/Ch
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="indigo"
            >
                <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-btn
                    fab
                    dark
                    small
                    color="red"
            >
                <v-icon>mdi-account-circle</v-icon>
            </v-btn>
        </v-speed-dial>
    </v-app>
</template>

<script>
    export default {
        name: "QuestionnaireEn",

        data() {
            return {
                ans: [],
                // 第一页问题的答案
                price: '',
                brand: [],
                purpose: '',
                rgb_require: '',
                bringout: '',
                screen: '',

                game: '',
                game_3A: '',
                software: '',
                study_purpose: '',


                //一线二线三线品牌硬编码
                first_brands: ['联想', 'ThinkPad', '戴尔', '苹果', '惠普', 'Acer', '索尼', '华硕', '微软', 'Alienware', 'HUAWEI', 'msi', 'ROG'],
                second_brands: ['三星', '神舟', '机械革命', 'Razer', 'Redmi', '雷神', '富士通', '东芝', '荣耀', '小米', '炫龙'],
                third_brands: ['同方', '方正', '七彩虹', 'a豆', '中柏', 'LG'],

                fab:false, //浮动按钮

                output: '',
                output_show: false,
                active_question: 0, // 激活题目的索引，从0开始
                degree: '',  // 控制进度条
                num_question: 6, // 总问题数
                num_ans: 0, //已回答问题数
                flag_addq2: false, //q2增加问题标志
                flag_addq3: false, //q3增加问题标志
            }
        },

        watch: {
            submit() {
                // Key名存储
                // let res = {
                //     price: this.price,
                //     purpose: this.purpose,
                //     brand: this.brand,
                //     // use_time: this.use_time,
                //     game: this.game,
                //     game_3A: this.game_3A,
                //     software: this.software,
                //     study_purpose: this.study_purpose,
                //     bringout: this.bringout,
                //     screen: this.screen,
                // }
                //
                // // 创建传输字符串
                // function create_res(res) {
                //     let values = Object.values(res);
                //     let res_str = '';
                //     let count = 0;
                //     for (let keys in res) {
                //         if (res_str === '') {
                //             res_str = keys + '=' + values[count];
                //         } else {
                //             res_str = res_str + '&' + keys + '=' + values[count];
                //         }
                //         count++;
                //     }
                //     return res_str;
                // }
                //
                // let res_str = create_res(res);
                // // console.log('post: ' + res_str);
                // // console.log('post: ' + JSON.stringify(res));
                //
                // fetch('http://127.0.0.1:5000/interface', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/x-www-form-urlencoded'
                //     }, // this line is important, if this content-type is not set it wont work
                //     body: res_str,
                // })
                //     .then(response => response.json())
                //     .then(response => {
                //         // for (let i = 0; i < Object.keys(response).length; i++)
                //         //     console.log('output: ' + JSON.stringify(response[i]));
                //
                //         this.output = response;
                //         console.log('output ' + JSON.stringify(this.output));
                //         console.log('output type' + typeof output);
                //     })

                // 跳转到下一页问卷
                this.$router.push(
                    {
                        name: 'Output',
                        params: {
                            price: this.price,
                            purpose: this.purpose,
                            brand: this.brand,
                            game: this.game,
                            game_3A: this.game_3A,
                            software: this.software,
                            study_purpose: this.study_purpose,
                            bringout: this.bringout,
                            screen: this.screen,
                        }
                    });
                // // 输出展示
                // this.output_show = true;
            },

            jump() {
                // 计算完成情况
                let count_ans = 0;
                let flag = {
                    price: this.price,
                    purpose: this.purpose,
                    rgb_require: this.rgb_require,
                    brand: this.brand,
                    // use_time: this.use_time,
                    game: this.game,
                    game_3A: this.game_3A,
                    software: this.software,
                    study_purpose: this.study_purpose,
                    bringout: this.bringout,
                    screen: this.screen,
                }
                // 更改问题总数
                // q2
                if (this.brand === 'none' && this.flag_addq2 == false) {
                    // this.num_question += 1;
                    this.flag_addq2 = true;
                } else if (this.brand === 'apple' && this.flag_addq2 == true) {
                    // this.num_question -= 1;
                    this.flag_addq2 = false;
                }
                // q3
                if ((this.purpose === 'work' || this.purpose === 'study' || this.purpose === 'game') && this.flag_addq3 == false) {
                    this.num_question += 1;
                    this.flag_addq3 = true;
                } else if (this.purpose === 'video' && this.flag_addq3 == true) {
                    this.num_question -= 1;
                    this.flag_addq3 = false;
                }


                for (let i = 0; i < Object.keys(flag).length; i++) {
                    if (Object.values(flag)[i] !== '') {
                        count_ans += 1
                    }
                }


                // console.log('now question is ' + length(this.active_question))

                // console.log('active question just now: ' + this.active_question)

                // console.log('active question now: ' + this.active_question)

                // 跳转到下一个问题
                this.active_question += 1

                // 控制进度条
                this.degree = count_ans / this.num_question * 100

            },
        },
    }
</script>

<style scoped>

</style>