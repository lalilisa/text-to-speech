import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { Login } from './admin/login'
import {Table} from './admin/table'
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
    return(
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/admin" element={<Table/>}/>
      </Routes>
      </BrowserRouter>
    )
}

export default App
