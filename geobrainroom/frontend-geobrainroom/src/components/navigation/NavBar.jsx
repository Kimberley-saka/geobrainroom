//import React from 'react'
import { useContext } from "react"
import { Link } from "react-router-dom"
import AuthContext from "../../context/AuthContext"

const NavBar = () => {
  let {name} = useContext(AuthContext)
  return (
    <div className='flex flex-row justify-between items-center px-5 h-16
    md:px-32 bg-slate-400'>

    <div>
      <p>GeoBrainRoom</p>
    </div>

    <div className='hidden flex-row text-base  justify-between items-center 
    w-2/4 h-full md:flex bg-slate-50'>
    <Link to='/'>Home</Link>
    <Link to='/login'>Login</Link>
    <p>Hello {name} </p>
    </div>
    </div>
    
  )
}

export default NavBar
