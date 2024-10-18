import React from 'react';
import {useForm} from "react-hook-form";
import {authService} from "../services/authService";

const LoginPage = () => {
    const {handleSubmit, register} = useForm();

    const submit = async (user) => {
        await authService.login(user)
    }

    return (
        <form onSubmit={handleSubmit(submit)}>
            <input type="text" placeholder={'email'} {...register('email')}/>
            <input type="text" placeholder={'password'} {...register('password')}/>
            <button>Login</button>
        </form>
    );
};

export default LoginPage;