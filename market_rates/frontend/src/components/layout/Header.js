import React, { Component } from 'react'

export class header extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-sm navbar-light bg-light">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
                <a className="navbar-brand" href="#">Cotizador</a>
                <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li><a href="">enlace 112 </a> </li>
                </ul>
            </div>
            </nav>
        )
    }
}

export default header
