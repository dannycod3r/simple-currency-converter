import React, { useState, useEffect } from 'react';
import './assets/money.jpg';

const CurrencyConverter = () => {
  const [fromCurrency, setFromCurrency] = useState('USD');
  const [toCurrency, setToCurrency] = useState('USD');
  const [amount, setAmount] = useState(1);
  const [convertedAmount, setConvertedAmount] = useState(0);

  const currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'NZD'];

  useEffect(() => {
    const fetchExchangeRate = async () => {
      try {
        const response = await fetch(
          `https://api.exchangeratesapi.io/latest?base=${fromCurrency}&symbols=${toCurrency}`
        );
        const data = await response.json();
        setConvertedAmount((amount * data.rates[toCurrency]).toFixed(2));
      } catch (error) {
        console.error('Error fetching exchange rate:', error);
      }
    };

    fetchExchangeRate();
  }, [fromCurrency, toCurrency, amount]);

  const handleFromCurrencyChange = (e) => {
    setFromCurrency(e.target.value);
  };

  const handleToCurrencyChange = (e) => {
    setToCurrency(e.target.value);
  };

  const handleAmountChange = (e) => {
    setAmount(e.target.value);
  };

  return (
    <div className="Container">
      <h2 className="heading">Currency Converter</h2>
      <main className="main">
        <section className="currency-converter">
          <div className="input-group">
            <label htmlFor="from-currency">From:</label>
            <select id="from-currency" name="from-currency" value={fromCurrency} onChange={handleFromCurrencyChange}>
              {currencies.map((currency) => (
                <option key={currency} value={currency}>
                  {currency}
                </option>
              ))}
            </select>

            <input
              type="number"
              id="amount"
              name="amount"
              value={amount}
              min="0"
              step="0.01"
              onChange={handleAmountChange}
            />
          </div>

          <div className="input-group">
            <label htmlFor="to-currency">To:</label>
            <select id="to-currency" name="to-currency" value={toCurrency} onChange={handleToCurrencyChange}>
              {currencies.map((currency) => (
                <option key={currency} value={currency}>
                  {currency}
                </option>
              ))}
            </select>
          </div>

          <button className="convert-btn">Convert</button>

          <div className="result">
            <p>
              <span id="converted-amount">{convertedAmount}</span>
              <span id="to-currency-symbol">{toCurrency}</span>
            </p>
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>&copy; 2024 Currency Converter</p>
      </footer>
    </div>
  );
};

export default CurrencyConverter;
