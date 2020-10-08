import React from 'react'
import { Switch, Route, BrowserRouter } from 'react-router-dom'
import NewRegister from './pages/NewRegister'
import Login from './pages/Login'
import Home from './pages/Home'





export default function Routes (){

    return(

        <BrowserRouter>
            <Switch>
                <Route path="/NewRegister" exact component={NewRegister} />
                <Route path="/Login" exact component={Login} />
                <Route path="/Home" exact component={Home} />
            </Switch>
        </BrowserRouter>
    )
}




