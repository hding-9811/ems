<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    update Emp info:{{$route.params.id}}
                </h1>

                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            id:
                        </td>
                        <td valign="middle" align="left">
                            {{$route.params.id}}
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            name:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="emp_list.emp_name"
                                   />
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            photo:
                        </td>
                        <td valign="middle" align="left">
                            <input type="file" name="photo" ref="photo"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            salary:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="salary" v-model="emp_list.salary"
                                  />
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            age:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="age" v-model="emp_list.age" />
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="button" value="Confirm" @click="update()"/>
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
        name: "UpdateEmp",
        data() {
            return {
                emp_list: [],
                emp_name: "",
                img: "",
                salary: "",
                age: ""

            }
        },
        methods: {
            findOne() {
                let id = this.$route.params.id
                console.log(id)
                this.$axios.get("http://127.0.0.1:8000/api/emp/" + `${id}` + "/").then(res => {
                    console.log(res.data.results);

                    this.emp_list = res.data.results
                    let a = this.emp_list
                    console.log(a["emp_name"])
                }).catch(error => {

                })
            },
            update() {
                let formData = new FormData();
                formData.append("emp_name", this.emp_list.emp_name);
                formData.append("img", this.$refs.photo.files[0]);
                formData.append("salary", this.emp_list.salary);
                formData.append("age", this.emp_list.age)
                this.$axios({
                    url: "http://127.0.0.1:8000/api/up/"+`${this.emp_list.id}`+'/',
                    method: "post",
                    data: formData,
                    headers: {
                        'content-type': 'multipart/form-data'
                    }

                }).then(res => {
                    this.$message({
                        message: '修改成功',
                        type: 'success'
                    });



                }).catch(error => {
                    this.$message.error("修改失败失败")

                })
            }
        },
        created() {
            let user = sessionStorage.getItem('user')
            if (user) {

            } else {
                this.$message.error("请登录")
                this.$router.push('/login')
            }
            this.findOne()

        }
    }
</script>

<style scoped>

</style>
