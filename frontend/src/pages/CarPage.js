import React from 'react';
import CarCreateComponent from "../components/Cars/CarCreateComponent";
import CarsComponent from "../components/Cars/CarsComponent";
import ChatComponent from "../components/Cars/ChatComponent";

const CarPage = () => {
    return (
        <div>
            <CarCreateComponent/>
            <hr/>
            <CarsComponent/>
            <hr/>
            <ChatComponent/>
        </div>
    );
};

export default CarPage;