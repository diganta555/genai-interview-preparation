import sqlite3
QUERY = """SELECT customer_id, SUM(amount_paise) AS total_paise
FROM orders WHERE tenant = ? AND purchased_on >= ? AND status = 'paid'
GROUP BY customer_id HAVING SUM(amount_paise) > ? ORDER BY customer_id LIMIT 100"""
def customers(conn, tenant, cutoff, threshold_paise=10000000):
    return conn.execute(QUERY,(tenant,cutoff,threshold_paise)).fetchall()
if __name__ == '__main__':
    with sqlite3.connect(':memory:') as conn:
        conn.execute('CREATE TABLE orders(tenant TEXT, customer_id TEXT, amount_paise INTEGER, purchased_on TEXT, status TEXT)')
        conn.executemany('INSERT INTO orders VALUES(?,?,?,?,?)',[
            ('demo','C1',7000000,'2026-06-01','paid'),
            ('demo','C1',4000000,'2026-08-01','paid'),
            ('demo','C2',9000000,'2026-07-01','paid'),
            ('other','C3',90000000,'2026-09-01','paid')])
        print(customers(conn,'demo','2026-04-03'))
        print('Cutoff is supplied explicitly; calendar-month subtraction is a business rule.')
