import './App.css';
import NavBar from './components/navigation/NavBar';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import { Route, Routes } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';

function App() {
 

  return (
    <>
    <AuthProvider>
      <NavBar/>
    </AuthProvider>
     
      <Routes>
        <Route element={<HomePage/>} path='/' exact/>
        <Route element={<LoginPage/>} path='/login'/>
      </Routes>
  </>
  )
}

export default App
