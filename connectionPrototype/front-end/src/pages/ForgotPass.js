import React, { Component } from 'react';

import LoggedInTester from '../buttons/LoggedInTester';


class ForgotPass extends Component {
    constructor(props) {
      super(props);
      this.state = { email: '',
                     auth_server: '',
                     auth_user: '',
                     auth_success: false,
                    };

      this.handleSubmitReg = this.handleSubmitReg.bind(this);
      this.handleSubmitAuth = this.handleSubmitAuth.bind(this);

      this.requestAuthCode = this.requestAuthCode.bind(this);
      this.checkAuthCode = this.checkAuthCode.bind(this);

      this.regForm = this.regForm.bind(this);
      this.authForm = this.authForm.bind(this);
    }


    handleSubmitReg(event) {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify({ password: this.state.password,
                                   email: this.state.email,
                                   })
        };

        fetch('http://127.0.0.1:8000/account/update_password/', requestOptions)
              .then(response => response.json())
              .then((data) => {
                this.setState({}, () => {
                    window.location.href = 'http://localhost:3000/login';
              })
        })
        .catch(console.log)

        event.preventDefault();
    }

    handleSubmitAuth(event) {
//        console.log("Yay");
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', },
            body: JSON.stringify({ email: this.state.email,
                                   mode: 'fpwd'})
        };

        fetch('http://127.0.0.1:8000/account/gen_auth/', requestOptions)
              .then(response => response.json())
              .then((data) => {
                    this.setState({ auth_server: data['auth_server'].toString(),
                                    auth_status: data['status']})
        })
        .catch(console.log)

        event.preventDefault();
    }

    requestAuthCode() {
        return(
        <>
            <form onSubmit = {this.handleSubmitAuth}>
                <input type="submit" value="Send Code" />
            </form> <br /> <br />
        </>
        )
    }

    checkAuthCode() {
        return(
        <>
            { this.state.auth_success ? <>Verification Success</> : <this.authForm /> }
            <br /> <br />
        </>
        )
    }

    authForm() {
        return(
        <>
            <>A Code Has Been Sent</>
            <form onSubmit = {(event) => { this.setState({ auth_success: (this.state.auth_user === this.state.auth_server) }); event.preventDefault();}}>
                <label>

                    Enter Your Verification Code Here:
                    <input type="text" value={this.state.auth_user} onChange={(event) =>
                                                                                {this.setState({ auth_user: event.target.value })}} />

                </label> <br />
                <input type="submit" value="Verify" />
            </form>
        </>
        )
    }

    regForm() {
        return (
        <>
            <form onSubmit={this.handleSubmitReg}>
                <label>
                    Password:
                    <input type="text" value={this.state.password} onChange={(event) =>
                                                                                {this.setState({ password: event.target.value })}} />
                </label> <br />

                {/* More robust error handling here? (Keep disabled until all fields non-empty) */}
                <input type="submit" value="Submit" disabled= {!this.state.auth_success} />
            </form>
        </>
        )
    }

    render() {
      return (
        <>

        <LoggedInTester />

        <label>
                    E-Mail:
                    <input type="text" value={this.state.email} disabled={this.state.auth_success}
                                        onChange={(event) => {this.setState({ email: event.target.value })}} />
        </label>

        { this.state.auth_status == 1 ? <> No user associated with this email </> : <></>}

        <br />

        {this.state.auth_server ?
            <this.checkAuthCode /> :
            <this.requestAuthCode />}

        <this.regForm />

        </>
      );
    }
  }

  export default ForgotPass
