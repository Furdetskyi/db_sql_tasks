import time
from app import db, UserModel, ProductModel

def benchmark_insert(user_count, product_count):
    start_time = time.time()
    for i in range(user_count):
        user = UserModel(username=f"user_{i}", password="password")
        db.session.add(user)
        db.session.commit()
        for j in range(product_count):
            product = ProductModel(
                name=f"product_{j}",
                brand=f"brand_{j}",
                price=round(j * 1.5, 2),
                user_id=user.id
            )
            db.session.add(product)
    db.session.commit()
    return time.time() - start_time

def benchmark_select():
    start_time = time.time()
    users = UserModel.query.all()
    products = ProductModel.query.all()
    return time.time() - start_time

def benchmark_update():
    start_time = time.time()
    users = UserModel.query.all()
    for user in users:
        user.username = f"updated_{user.username}"
    db.session.commit()
    return time.time() - start_time

def benchmark_delete():
    start_time = time.time()
    ProductModel.query.delete()
    UserModel.query.delete()
    db.session.commit()
    return time.time() - start_time

if __name__ == "__main__":
    db.create_all()

    for records in [1000, 10000, 100000, 1000000]:
        print(f"\nBenchmark for {records} records:")
        insert_time = benchmark_insert(records, 10)
        print(f"INSERT: {insert_time:.2f} seconds")
        
        select_time = benchmark_select()
        print(f"SELECT: {select_time:.2f} seconds")
        
        update_time = benchmark_update()
        print(f"UPDATE: {update_time:.2f} seconds")
        
        delete_time = benchmark_delete()
        print(f"DELETE: {delete_time:.2f} seconds")