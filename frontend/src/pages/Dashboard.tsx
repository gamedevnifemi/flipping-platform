/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useEffect, useState } from "react";
import axios from "axios";
import DashboardLayout from "../layouts/Dashboard";

interface Product {
    id: number;
    title: string;
    marketplace: string;
    price: number;
    last_updated: string;
}

const Dashboard: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);
    const [loading, setLoading] = useState(true);
    const apiUrl = import.meta.env.VITE_PRODUCT_API_URL;

    useEffect(() => {
        axios.get(apiUrl, {
            withCredentials: true
        })
        .then(response => {
            setProducts(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error('Error fetching data: ', error);
            setLoading(false);
        });
    }, []);

    return (
        <DashboardLayout>
            <div className="p-6">
                <h1 className="text-3xl font-bold text-gray-800 mb-8">Dashboard</h1>
                {loading ? (
                    <div className="flex justify-center">
                        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {products.map((product) => (
                            <div key={product.id} className="bg-white rounded-lg shadow p-6">
                                <h3 className="text-lg font-semibold mb-2">{product.title}</h3>
                                <p className="text-gray-600">{product.marketplace}</p>
                                <p className="text-2xl font-bold text-blue-600 mt-2">£{product.price}</p>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </DashboardLayout>
    );
};

export default Dashboard;