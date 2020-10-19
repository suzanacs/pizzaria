import React, {useState} from 'react'
import { Grid, Cell, Card, CardText, TextField, DatePicker, Button  } from 'react-md';
import api from '../../services/api'
import moment from 'moment'
import {cpfMask} from '../../utils/cpfMask'
import {cepMask} from '../../utils/cepMask'
import {phoneMask} from '../../utils/phoneMask'


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
    const [celPhone, setcelPhone] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')

    async function handleNewRegister() {

        if(password===confirmPassword){
            
            const response = await api.post('/users', {
                'nome': name,
                'cpf': cpf,
                'celular': celPhone,
                'dtNasc': dataNasc, 
                'email': email,
                'senha': password,
                'endereco': {
                    'rua': street,
                    'numero': numHouse,
                    'cep': cep,
                    'bairro': bairro,
                    'cidade': city,
                    'estado': state
                }        
            })
        
            console.log(response.data)
            console.log(response)
            if(response.data.data){
                alert("Cadastro realizado com sucesso!")
            }   
            else {
                alert('Email/CPF já cadastrado(s)!')
            }
        }else{
            alert("as senhas não são iguais")
        }
    }
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
                           maxLength={90} 
                           value={name}
                           onChange={event => setName(event.valueOf('name'))}                 
                        />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={2}>
                        <DatePicker
                            id="dataNasc"
                            label="Data de Nascimento"
                            onChange={val => setDataNasc(moment(val, 'DD/MM/YYYY').toISOString(true).substring(0, 10), 'dataNasc')}
                            formatOptions={{ year: 'numeric', month: 'numeric', day: 'numeric' }}
                        />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={4}>
                            <TextField 
                                id='cpf'
                                label='CPF'
                                type='text'
                                maxLength={15}
                                value={cpf}
                                onChange={event => setCpf(cpfMask(event.valueOf('cpf')))}
                            />
                        </Cell>
                    </Grid>
                    <Grid>
                        <Cell desktopSize={7} tabletSize={8}>
                            <TextField 
                                id='street'
                                label='Rua'
                                type='text'
                                maxLength={90}
                                value={street}
                                onChange={event => setStreet(event.valueOf('street'))}
                            />
                        </Cell>
                        <Cell desktopSize={1} tabletSize={2}>
                            <TextField 
                                id='numHouse'
                                label='Número'
                                type='number'
                                maxLength={6}
                                value={numHouse}
                                onChange={event => setNumHouse(event.valueOf('numHouse'))}

                            />
                        </Cell>
                        <Cell desktopSize={3} tabletSize={2}>
                            <TextField 
                                id='cep'
                                label='CEP'
                                type='text'
                                value={cep}
                                maxLength={9}
                                onChange={event => setCep(cepMask(event.valueOf('cep')))}
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
                                maxLength={30}
                                onChange={event => setBairro(event.valueOf('bairro'))}
                            />
                        </Cell>
                        <Cell desktopSize={4} tabletSize={5}>
                            <TextField 
                                id='city'
                                label='Cidade'
                                type='text'
                                value={city}
                                maxLength={30}
                                onChange={event => setCity(event.valueOf('city'))}
                            />
                        </Cell>
                        <Cell desktopSize={1} tabletSize={2}>
                            <TextField 
                                id='state'
                                label='Estado'
                                type='text'
                                value={state}
                                maxLength={2}
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
                            maxLength={60}
                            onChange={event => setEmail(event.valueOf('email'))}
                        /> 
                        </Cell>
                        <Cell desktopSize={4} tabletSize={5}>
                        <TextField
                            id='celPhone'
                            label='Celular'
                            type='text'
                            value={celPhone}
                            maxLength={15}
                            onChange={event => setcelPhone(phoneMask(event.valueOf('celPhone')))}
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
                        <Button flat primary swapTheming onClick={handleNewRegister}>Cadastrar</Button>
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