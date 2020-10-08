import React from 'react'
import {Grid, Cell, Card, CardText} from 'react-md'


const style = {maxWidth: 1100}

const Home = () => {

    return(
    <>
   <Grid style={style}>
        <Cell size={12}>
            <Card>
                <CardText>
                    <h1>Universo da Pizza</h1>
                </CardText>
            </Card>
        </Cell>
   </Grid>
    </>
    )
}



export default Home