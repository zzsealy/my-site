<script type="text/javascript">
    const URL = "http://localhost:8001";
    export default
    {
      URL,
      state: {
        is_login: window.localStorage.getItem('mysite-token') ? true : false,
        user_id: window.localStorage.getItem('mysite-user-id')
      },
      loginActinon(){
        this.is_login = true;
      },
      logoutAction(){
        window.localStorage.removeItem('mysite-token')
        window.localStorage.removeItem('mysite-user-id')
        this.state.is_login = false;
        this.state.user_id = 0;
      }
    }

</script>