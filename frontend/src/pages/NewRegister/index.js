import React, {useState} from 'react'
import { Grid, Cell, Card, CardText, TextField, DatePicker, Button  } from 'react-md';

import {Link} from 'react-router-dom'

const style = { maxWidth: 1200 };

const NewRegister = () => {

    const [name, setName] = useState('') 
    const [dataNasc, setDataNasc] = useState('')
    const [cpf, setCpf] = useState('')
    const [street, setStreet] = useState('')
    const [numHouse, setNumHouse] = useState('')
    const [cep, setCep] = useState('')
    const [bairro, setBairro] = useState('')
    const [city, setCity] = useState('')
    const [state, setState] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')

    return(
      
       
    <Grid style={style}> 
        <Cell size={12}>
            <h1 className='md-headeline'>Cadastro</h1>
            <Card>
                <CardText>
                    <Grid>
                        <Cell desktopSize={5} tabletSize={6}>
                        <TextField
                           id='name'
                           label='Nome completo'
                           placeholder='Nome Completo'     
                           value={name}
                           onChange={event => setName(event.valueOf('name'))}                 
                        />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={2}>
                        <DatePicker
                            id="dataNasc"
                            label="Data de Nascimento"
                            value={dataNasc}
                            onChange={event => setDataNasc(event.valueOf('dataNasc'))}
                        />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={4}>
                            <TextField 
                                id='cpf'
                                label='CPF'
                                type='text'
                                value={cpf}
                                onChange={event => setCpf(event.valueOf('cpf'))}
                            />
                        </Cell>
                    </Grid>
                    <Grid>
                        <Cell desktopSize={7} tabletSize={8}>
                            <TextField 
                                id='street'
                                label='Rua'
                                type='text'
                                value={street}
                                onChange={event => setStreet(event.valueOf('street'))}
                            />
                        </Cell>
                        <Cell desktopSize={1} tabletSize={2}>
                            <TextField 
                                id='numHouse'
                                label='Número'
                                type='number'
                                value={numHouse}
                                onChange={event => setNumHouse(event.valueOf('numHouse'))}

                            />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={2}>
                            <TextField 
                                id='cep'
                                label='CEP'
                                type='number'
                                value={cep}
                                onChange={event => setCep(event.valueOf('cep'))}
                            />
                        </Cell>
                    </Grid>
                    <Grid>
                        <Cell desktopSize={3} tabletSize={4}>
                            <TextField 
                                id='bairro'
                                label='Bairro'
                                type='text'
                                value={bairro}
                                onChange={event => setBairro(event.valueOf('bairro'))}
                            />
                        </Cell>
                        <Cell desktopSize={4} tabletSize={5}>
                            <TextField 
                                id='city'
                                label='Cidade'
                                type='text'
                                value={city}
                                onChange={event => setCity(event.valueOf('city'))}
                            />
                        </Cell>
                        <Cell desktopSize={4} tabletSize={5}>
                            <TextField 
                                id='state'
                                label='Estado'
                                type='text'
                                value={state}
                                onChange={event => setState(event.valueOf('state'))}
                            />
                        </Cell>
                    </Grid>
                    <Grid>
                        <Cell desktopSize={7} tabletSize={8}>
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
                        <Cell desktopSize={5} tabletSize={4}>  
                        <TextField
                            id='password'
                            label='Senha'
                            type='password'
                            value={password}
                            onChange={event => setPassword(event.valueOf('password'))}
                        />                          
                        </Cell>
                        <Cell desktopSize={5} tabletSize={6}>
                            <TextField 
                                id='confirmPassword'
                                label='Confirme a senha'
                                type='password'
                                value={confirmPassword}
                                onChange={event => setConfirmPassword(event.valueOf('confirmPassword'))}
                            />
                        </Cell>
                    </Grid>
                    <Grid>
                    <Cell desktopSize={2} tabletSize={2}>
                        <Button flat primary swapTheming onClick={()=>{console.log(name,dataNasc,cpf,street,numHouse,cep,bairro,city,state,email,password,confirmPassword)}}>Cadastrar</Button>
                    </Cell>
                    <Cell desktopSize={2} tabletSize={2}>
                        <Button flat primary swapTheming
                            component={Link}
                            to='/Login'>Login</Button>
                    </Cell>
                    </Grid>
                </CardText>
            </Card>
        </Cell>
    </Grid>
   
       
    )
}


export default NewRegister