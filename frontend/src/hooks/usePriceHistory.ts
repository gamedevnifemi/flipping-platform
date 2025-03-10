import { useState, useEffect } from "react";
import axios from "axios";

interface PriceHistoryEntry {
    date: string;
    stockX_price: number;
    goat_price: number;
}

const usePriceHistory = (sneakerId: number) => {
    const [priceHistory, setPriceHistory] = useState<PriceHistoryEntry[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchPriceHistory = async () => {
            try {
                setLoading(true);
                const apiUrl = import.meta.env.VITE_PRODUCT_API_URL;
                const response = await axios.get(`${apiUrl}price/history/${sneakerId}`);
                setPriceHistory(response.data.price_history);
                setError(null);
            } catch (error) {
                console.error("Error fetching price history", error);
                setError("Failed to load price history");
                // Set some dummy data for development if needed
                setPriceHistory([
                    { date: "2025-01-01", stockX_price: 200, goat_price: 210 },
                    { date: "2025-01-15", stockX_price: 220, goat_price: 225 },
                    { date: "2025-01-30", stockX_price: 215, goat_price: 230 },
                    { date: "2025-02-15", stockX_price: 230, goat_price: 240 }
                ]);
            } finally {
                setLoading(false);
            }
        };

        fetchPriceHistory();
    }, [sneakerId]);

    return { priceHistory, loading, error };
};

export default usePriceHistory;
