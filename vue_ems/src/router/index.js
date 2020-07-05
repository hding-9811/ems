import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Index from "../components/Index";
import Addemp from "../components/Addemp";
import UpdateEmp from "../components/UpdateEmp";


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: "/",
            name: "Login",
            component: Login
        },
        {
            path: "/login",
            name: "Login",
            component: Login
        },
        {
            path: "/register",
            name: "register",
            component: Register
        },
        {
            path:"/index",
            name:"index",
            component:Index
        },
        {
            path:"/addemp",

            name:"addemp",
            component:Addemp
        },
        {
            path:"/update",
            name:"update",
            component:UpdateEmp
        },
        {
            path:"/update/:id",
            name:"update",
            component:UpdateEmp
        },
    ]
})
