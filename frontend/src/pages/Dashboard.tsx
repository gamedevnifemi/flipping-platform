/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState } from "react";
import DashboardLayout from "../layouts/Dashboard";
import usePriceHistory from "../hooks/usePriceHistory";
import PriceChart from "../components/PriceChart";

const Dashboard = () => {
    // Default to showing the first sneaker or allow user to select one
    const [selectedSneakerId, setSelectedSneakerId] = useState<number>(1);
    const { priceHistory, loading } = usePriceHistory(selectedSneakerId);

    return (
        <DashboardLayout>
            <div className="p-6">
                <h1 className="text-3xl font-bold text-gray-800 mb-8">Dashboard</h1>
                
                {/* Add selector for different sneakers */}
                <div className="mb-6">
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                        Select Sneaker:
                    </label>
                    <select
                        className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                        value={selectedSneakerId}
                        onChange={(e) => setSelectedSneakerId(Number(e.target.value))}
                    >
                        <option value={1}>Jordan 1 Retro</option>
                        <option value={2}>Yeezy 350</option>
                        <option value={3}>Nike Dunk Low</option>
                    </select>
                </div>
                
                <div className="p-6 bg-white rounded-lg shadow-md">
                    <h2 className="text-xl font-bold mb-4">Sneaker Market Trends</h2>
                    
                    {loading ? (
                        <div className="flex justify-center py-10">
                            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
                        </div>
                    ) : (
                        <PriceChart priceHistory={priceHistory} />
                    )}
                </div>
            </div>
        </DashboardLayout>
    );
};

export default Dashboard;
