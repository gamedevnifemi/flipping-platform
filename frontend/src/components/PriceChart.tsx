import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

interface PriceHistoryEntry {
    date: string;
    stockX_price: number;
    goat_price: number;
}

interface PriceChartProps {
    priceHistory: PriceHistoryEntry[];
}

const PriceChart = ({ priceHistory }: PriceChartProps) => {
    if (!priceHistory || priceHistory.length === 0) {
        return (
            <div className="flex justify-center items-center p-10 border rounded-lg bg-gray-50">
                <p className="text-gray-500">No price history available for this product.</p>
            </div>
        );
    }

    const data = {
        labels: priceHistory.map((entry) => entry.date),
        datasets: [
            {
                label: "StockX Prices",
                data: priceHistory.map((entry) => entry.stockX_price),
                borderColor: "green",
                fill: false
            },
            {
                label: "GOAT Prices",
                data: priceHistory.map((entry) => entry.goat_price),
                borderColor: "black",
                fill: false
            }
        ]
    };

    return <Line data={data} />;
};

export default PriceChart;
