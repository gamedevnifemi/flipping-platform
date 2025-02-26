import React, { useEffect, useState } from "react";
import axios from "axios";
import ProductCard from "../components/ProductCard";
import DashboardLayout from "../layouts/Dashboard";

interface Sneaker {
    id: number;
    style_id: string;
    shoe_name: string;
    retail_price: string;
    thumbnail: string;
    description?: string;
    brand?: string;
    colorway?: string;
    stockx_url: string;
    goat_url: string;
    last_updated: string;
}

const Products = () => {
    const [sneakers, setSneakers] = useState<Sneaker[]>([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState("");
    const [platform, setPlatform] = useState("");

    useEffect(() => {
        const fetchSneakers = async () => {
            try {
                const apiUrl = import.meta.env.VITE_PRODUCT_API_URL;
                const response = await axios.get<Sneaker[]>(
                    apiUrl,
                    { withCredentials: true }
                );
                setSneakers(response.data);
            } catch (error) {
                console.error("Error fetching sneakers", error);
            } finally {
                setLoading(false);
            }
        };

        fetchSneakers();
    }, []);

    return (
        <DashboardLayout>
            <div className="min-h-screen bg-gray-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                    {/* Header Section */}
                    <div className="mb-8">
                        <h1 className="text-4xl font-bold text-gray-900 mb-4">Sneaker Market</h1>
                        <p className="text-gray-600">Track and compare prices across multiple platforms</p>
                    </div>

                    {/* Search and Filter Section */}
                    <div className="bg-white rounded-lg shadow-sm p-4 mb-8">
                        <div className="flex flex-col md:flex-row gap-4">
                            <div className="flex-1">
                                <input
                                    type="text"
                                    placeholder="Search by name, brand, or style..."
                                    value={searchTerm}
                                    onChange={(e) => setSearchTerm(e.target.value)}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                />
                            </div>
                            <div className="w-full md:w-48">
                                <select 
                                    value={platform}
                                    onChange={(e) => setPlatform(e.target.value)}
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                >
                                    <option value="">All Platforms</option>
                                    <option value="stockx">StockX</option>
                                    <option value="goat">GOAT</option>
                                    <option value="ebay">eBay</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    {/* Products Grid */}
                    {loading ? (
                        <div className="flex justify-center items-center h-64">
                            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
                        </div>
                    ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            {sneakers.map((sneaker) => (
                                <ProductCard
                                    key={sneaker.id}
                                    product={{
                                        id: sneaker.style_id,
                                        name: sneaker.shoe_name,
                                        price: sneaker.retail_price,
                                        thumbnail: sneaker.thumbnail,
                                        brand: sneaker.brand,
                                        colorway: sneaker.colorway,
                                        resellLinks: {
                                            stockx: sneaker.stockx_url,
                                            goat: sneaker.goat_url
                                        }
                                    }}
                                />
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default Products;
