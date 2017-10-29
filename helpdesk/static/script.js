Vue.component('nav-option', {
    template: '<div><slot></slot></div>'
})

Vue.component('nav-list', {
    template: '<div class="sidebar"><span class="title">Support Categories</span><nav-option v-for="item in items" :class="{activeoption : item.active}"><a :href=item.link class="sideoption"><div class="sidebar-item"><span class="type">{{item.name}}</span><span class="count">{{item.count}}</span></div></a></nav-option></div>',
    data: function () {
        return {
            items: [
                {
                    name: 'Where is my order',
                    count: '12',
                    link: 'index.html',
                    active: true
                },
                {
                    name: 'Problem with my order',
                    count: '9',
                    link: '#',
                    active: false
                },
                {
                    name: 'Return and refund',
                    count: '5',
                    link: '#',
                    active: false
                }, {
                    name: 'Change or cancel order',
                    count: '2',
                    link: '#',
                    active: false
                }, {
                    name: 'Payment Issues',
                    count: '11',
                    link: '#',
                    active: false
                }, {
                    name: 'Seller Issues',
                    count: '22',
                    link: '#',
                    active: false
                }, {
                    name: 'Delivery Issues',
                    count: '17',
                    link: '#',
                    active: false
                }, {
                    name: 'Promotion and deals',
                    count: '14',
                    link: '#',
                    active: false
                }, {
                    name: 'More Order Issues',
                    count: '4',
                    link: '#',
                    active: false
                },
            ]
        }
    }
})

Vue.component('ticket-option', {
    template: '<div><slot></slot></div>'
})

Vue.component('ticket-list', {
    template: '<div class="tickets"><ticket-option v-for="item in items" class="ind"><span class="name">{{item.name}}</span><br/><span class="issue">{{item.issue[0]}}</span></a></ticket-option></div>',
    data: function () {
        return {
            items: [
                {
                    name: 'Sarthak Pattanayak',
                    issue: ['I bought a Lenovo gaming headphones this summer. Order id: OD109205149477701000. Now the right side speakers dont work anymore....I would like to apply for warranty(the item is well within the warranty period).', 'Well fuck you flipkart'],
                    replies: []

                },
                {
                    name: 'Ravi Mirchandani',
                    issue: ['order id OD110399722905504000 cancelled as it was under an exchange , and the exchange piece was damaged by flipkart.focefully cancelled my order for which payment was made through bajaj fin emi. order cancelled on 08.10.2017 but still getting sms about emi due  the cancelled order', 'Thanks for responding nigga'],
                    replies: []
                },
                {
                    name: 'Abhi silani',
                    issue: ['Order ID: OD110564436656024000 Product(s): Unistuff Tempered Glass Guard for Mi Redmi Note 4, Redmi Note 4 (Black, 64 GB) and Kapaver Back Cover for Xiaomi Redmi Note 4. Flipkart cancelled the order without my authorization on 23rd Oct 2017. They wrote to me that amount has been refunded in my bank account on 25th october 2017, however, i checked with my HSBC bank in dubai (i have a record for conversation) that the amount is not yet credited. The response from flipkart is indifferent and usually too late', 'I already died asshole'],
                    replies: []
                }
            ]
        }
    }
})



var en0 = new Vue({
    el: '#root'
})
