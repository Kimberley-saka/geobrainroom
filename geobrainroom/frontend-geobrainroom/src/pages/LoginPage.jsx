//import React from 'react'

const LoginPage = () => {
  return (
    <div className='flex flex-col gap-5 justify-center items-center mt-36'>
      <div className="flex max-w-2/3 bg-slate-400">
      <p>Dont have an account <a href="">Create your account?</a></p>
      </div>
      
      <form className='flex flex-col gap-5 justify-center text-center items-center h-3/4'>
        <input type='text' name='username' placeholder='Username'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2 w-90'
        ></input>
        <input type='email' name='email' placeholder='Email'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2 max-w-72'></input>
        <input type='text' name='password' placeholder='Password'
        className='border-2 border-gray-300 rounded-lg h-10 pl-2 max-w-72'></input>
        <button type='submit' className='w-32 bg-sky-800 text-white
        h-10 rounded-full'>Submit</button>

      </form>
    </div>
  )
}

export default LoginPage
