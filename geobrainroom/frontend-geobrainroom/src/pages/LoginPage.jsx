import {useContext} from 'react'
import AuthContext from '../context/AuthContext'


const LoginPage = () => {
  let {loginUser} = useContext(AuthContext)
  return (
    <div className='flex flex-col gap-5 justify-center items-center mt-24'>
      <div className='flex flex-col gap-5 items-start
      border-transparent shadow-2xl rounded-2xl md:w-1/3'>
        <div className='flex justify-center items-center w-full mb-5
        bg-sky-800 rounded-t-2xl h-14'>
          <p className='text-lg font-bold text-white'>Welcome</p>
        </div>
      
      <form onSubmit={loginUser} className='flex flex-col gap-5 w-full px-4'>
        <input type='text' name='username' placeholder='Username'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2'
        ></input>
        <input type='email' name='email' placeholder='Email'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2 max-w-72'></input>
        <input type='text' name='password' placeholder='Password'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2 max-w-72'></input>
      
        <button type='submit' className=' bg-sky-800 text-white
        h-10 rounded-full w-full'>Login</button>

      </form>

      <div className="flex flex-col justify-center items-center w-full gap-2 px-4">
        <p className='text-gray-500'>Don&apos;t have an account?</p>
        <a href="/signup" className='text-sky-800'><p>Sign up</p> </a>
      </div>
      </div>

    </div>
  )
}

export default LoginPage
