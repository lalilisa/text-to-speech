
import '../admin/css/login/login.css'
export const Login=()=>{
    return (
        <>
        <div class="login-box">
        <h2>Login</h2>
        <form>
          <div class="user-box">
            <input type="text" name="" required="" placeholder='username'/>
          </div>
          <div class="user-box">
            <input type="text" placeholder='password'/>
          </div>
          <div className='button' >
          <a href="#">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            Login
          </a>
          </div>
        </form>
      </div>
      </>
    )
}