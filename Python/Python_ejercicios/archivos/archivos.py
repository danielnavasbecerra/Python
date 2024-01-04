from csv import DictWriter

def write_reservations(f, reservations, headers):
    with open(f,"w", newline='') as f2:
        writer = DictWriter(f2,  fieldnames = headers )
        if headers:
            writer.writeheader()
        for reservation in reservations:
            writer.writerow({
                'availability_zone': reservation["availability_zone"],
                'tenancy': reservation["tenancy"],
                'product': reservation["product"],
                'cost_hourly': reservation["cost_hourly"],
                'cost_upfront': reservation["cost_upfront"],
                'count': reservation["count"],
                'count_used': reservation["count_used"],
            })

headers = [
        'availability_zone',
        'tenancy',
        'product',
        'cost_hourly',
        'cost_upfront',
        'count',
        'count_used',
        ]
reservations = [
            {"availability_zone" : 2,
                 "tenancy": 3,
                 'product': 1,
                 'cost_hourly': 3500,
                 'cost_upfront':  4800,
                 "count": 45,
                 "count_used":1
            },{"availability_zone" : 3,
                 "tenancy": 3,
                 'product': 4,
                 'cost_hourly': 3700,
                 'cost_upfront':  5800,
                 "count": 25,
                 "count_used":13
            }]

write_reservations("Python/Python_ejercicios/archivos/reservations.csv", reservations, headers)