<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <router-link to="/login">安全退出</router-link>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    欢迎{{user_msg}}
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>

                    <tr class="row2" v-for="(emp,index) in emp_list" :key="emp.id" :class="index%2==0?'row1':'row2'">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img :src="emp.img" style="height: 60px;"></td>
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td>
                            <a href="javascript:void(0)" @click="del(emp.id)">删除</a>
                            &nbsp;
                            <router-link :to="'/update/'+emp.id">更新</router-link>
                        </td>
                    </tr>
                </table>
                <p>
<!--                    <input type="button" class="button" value="Add Employee"/>-->
                                        <router-link to="/addemp">添加员工</router-link>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Index",
        data() {
            return {
                user_msg: '',
                emp_list: [],


            }
        },
        methods: {
            //获取所有员工信息
            findsAll() {
                this.$axios({
                    url: "http://127.0.0.1:8000/api/emp/",
                    method: "get",
                    params: {}

                }).then(res => {
                    console.log(res.data.results)
                    this.emp_list = res.data.results


                }).catch(error => {

                })
            },
            del(id) {

                this.$axios({
                    url: "http://127.0.0.1:8000/api/emp/" + `${id}`,
                    method: "delete",

                }).then(res => {
                    this.$message({
                        message: '删除成功',
                        type: 'success'
                    });
                }).catch(error => {
                    this.$message.error('删除失败');
                })
            }
        },

        created() {
            let username = sessionStorage.getItem('user')

            if (username) {
                this.user_msg = username


            } else {
                this.$message.error("请登录")
                this.$router.push('/login')
            }
            this.findsAll()
        }
    }
</script>

<style scoped>

</style>
