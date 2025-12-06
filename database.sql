-- Membuat tabel Review
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,          -- ID review otomatis bertambah
    review_text TEXT NOT NULL,      -- Teks review produk
    sentiment VARCHAR(20) NOT NULL, -- Sentimen dari review (positive, negative, neutral)
    key_points TEXT                 -- Poin-poin penting dari review
);

-- Menambahkan index pada kolom review_text untuk pencarian yang lebih cepat
CREATE INDEX idx_review_text ON reviews(review_text);

-- Menambahkan review baru
INSERT INTO reviews (review_text, sentiment, key_points)
VALUES
('This product is amazing! I love how easy it is to use.', 'POSITIVE', 'Amazing product, easy to use'),
('The product was okay, but it didn`t meet my expectations.', 'NEUTRAL', 'Okay product, unmet expectations'),
('Terrible product, didn`t work as expected.', 'NEGATIVE', 'Terrible product, didn`t work');
