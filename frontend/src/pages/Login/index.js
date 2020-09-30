import React, {useState} from 'react'
import {Grid, Cell, Card, CardText, TextField, Button} from 'react-md'
import { Link} from "react-router-dom"

const style = { maxWidth: 500}

const Login = ({navigation}) =>{

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')


    return(
        <Grid style={style}>
            <Cell size={12}>
                <h1 className='md-headeline'>Login</h1>
                <Card>
                    <CardText>
                        <Grid>
                            <Cell desktopSize={8} tabletSize={7}>
                                <TextField
                                id='email'
                                label='Email'
                                type='email'
                                value={email}
                                onChange={event => setEmail(event.valueOf('email'))}
                                />
                            </Cell>
                        </Grid>
                        <Grid>
                            <Cell desktopSize={8} tabletSize={7}>
                            <TextField
                            id='password'
                            label='Senha'
                            type='password'
                            value={password}
                            onChange={event => setPassword(event.valueOf('password'))}
                        />       
                            </Cell>
                        </Grid>
                        <Grid>
                            <Cell desktopSize={6} tabletSize={7}>
                                <Button flat primary swapTheming onClick={() => {console.log(email,password)}}>Entrar</Button>
                            </Cell>
                        </Grid>
                        <Grid>
                            <Cell desktopSize={6} tabletSize={7}>
                            <Button flat>Esqueceu sua senha?</Button>
                            </Cell>
                       
                            <Cell desktopSize={6} tabletSize={7}>
                            <Button flat primary 
                            component={Link}
                            to="/NewRegister">Cadastre-se</Button>
                            </Cell>
                        </Grid>
                    </CardText>
                </Card>
            </Cell>
        </Grid>
    )
}

export default Login