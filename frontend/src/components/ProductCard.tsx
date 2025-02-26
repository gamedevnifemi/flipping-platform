interface Product {
    id: string;
    name: string;
    price: string;
    thumbnail: string;
    description?: string;
    brand?: string;
    colorway?: string;
    resellLinks: {
        stockx: string;
        goat: string;
    };
}

const ProductCard: React.FC<{ product: Product }> = ({ product }) => {
    return (
        <div className="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden">
            {/* Image Container */}
            <div className="relative aspect-square">
                <img 
                    src={product.thumbnail || 'placeholder-image.jpg'} 
                    alt={product.name}
                    className="w-full h-full object-cover"
                />
                {product.brand && (
                    <div className="absolute top-4 left-4">
                        <span className="bg-black bg-opacity-75 text-white px-3 py-1 rounded-full text-sm">
                            {product.brand}
                        </span>
                    </div>
                )}
            </div>

            {/* Content Container */}
            <div className="p-6">
                <div className="mb-4">
                    <h2 className="text-xl font-bold text-gray-900 mb-2 line-clamp-2">
                        {product.name}
                    </h2>
                    {product.colorway && (
                        <p className="text-sm text-gray-600">
                            {product.colorway}
                        </p>
                    )}
                </div>

                <div className="flex justify-between items-end">
                    <div>
                        <p className="text-sm text-gray-500">Retail Price</p>
                        <p className="text-2xl font-bold text-blue-600">
                            ${parseFloat(product.price).toFixed(2)}
                        </p>
                    </div>
                    
                    <div className="flex flex-col space-y-2">
                        <button 
                            onClick={() => window.open(product.resellLinks.stockx, '_blank')}
                            className="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition-colors duration-300 text-sm flex items-center gap-2"
                        >
                            <span>StockX</span>
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                            </svg>
                        </button>
                        
                        {product.resellLinks.goat && (
                            <button 
                                onClick={() => window.open(product.resellLinks.goat, '_blank')}
                                className="px-4 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-700 transition-colors duration-300 text-sm flex items-center gap-2"
                            >
                                <span>GOAT</span>
                                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                                </svg>
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ProductCard;
