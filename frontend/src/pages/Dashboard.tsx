/* eslint-disable @typescript-eslint/no-explicit-any */
import React,{ useEffect, useState } from "react";
import axios from "axios";

interface Product {
    id: number;
    name: string;
    marketplace: string;
    price: number;
    last_updated: string;
}

const Dashboard: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);
    const [error] = useState<string | null>(null);

    useEffect(() => {
        axios.get("http://localhost:8000/api/products", {
            withCredentials: true
        })
        .then(response => setProducts(response.data))
        .catch(error => console.error('Error fetching data: ', error));
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>
            {error && <p>{error}</p>}
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                    {product.name} - {product.marketplace} - ${product.price}
                </li>
                ))}
            </ul>
        </div>
    );
}
export default Dashboard;