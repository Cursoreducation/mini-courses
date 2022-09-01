class PostDB:
    storage = [
        {
            "id": 1,
            "title": "Dell виходить з росії та звільняє усіх співробітників там",
            "text": """Одна з найбільших компаній із виробництва компʼютерів та серверів Dell остаточно йде з ринку росії. Разом з тим корпорація звільняє весь штат співробітників там, пише Forbes з посиланням на російські медіа.

            Dell планує завершити роботу в рф наприкінці серпня. Компанія збиралася розвивати центр розробок у санкт-петербурзі, але тепер перемкнулася на центр розробок у Польщі.
            
            Загалом у російському представництві працюють близько 50 осіб. Dell може виплатити до восьми окладів співробітникам під час звільнення, а комусь залишать медстрахування на сімʼю до кінця року. Колишні працівники компанії кажуть, що техніку їм дозволили залишити собі, але всі дані корпорація видаляє із жорстких дисків та корпоративних телефонів.
            
            Видання пише, що, за словами гендиректора російської компанії з виробництва інноваційних рішень «Аеродиск» Вʼячеслава Володковича, вихід Dell змусить частину замовників перейти на російські рішення, «беручи на себе всі ризики, повʼязані з нестачею необхідних обсягів виробництва». Хтось шукатиме рішення в паралельному імпорті, тобто «сірому» ринку (у травні російський уряд дозволив компаніям ввозити товари для внутрішнього ринку без погодження з їх виробниками).
            """
        },
        {
            "id": 2,
            "title": "Dell виробила ноутбук",
            "text": """Одна з найбільших компаній із виробництва компʼютерів та серверів Dell остаточно йде з ринку росії. Разом з тим корпорація звільняє весь штат співробітників там, пише Forbes з посиланням на російські медіа.

                Dell планує завершити роботу в рф наприкінці серпня. Компанія збиралася розвивати центр розробок у санкт-петербурзі, але тепер перемкнулася на центр розробок у Польщі.

                Загалом у російському представництві працюють близько 50 осіб. Dell може виплатити до восьми окладів співробітникам під час звільнення, а комусь залишать медстрахування на сімʼю до кінця року. Колишні працівники компанії кажуть, що техніку їм дозволили залишити собі, але всі дані корпорація видаляє із жорстких дисків та корпоративних телефонів.

                Видання пише, що, за словами гендиректора російської компанії з виробництва інноваційних рішень «Аеродиск» Вʼячеслава Володковича, вихід Dell змусить частину замовників перейти на російські рішення, «беручи на себе всі ризики, повʼязані з нестачею необхідних обсягів виробництва». Хтось шукатиме рішення в паралельному імпорті, тобто «сірому» ринку (у травні російський уряд дозволив компаніям ввозити товари для внутрішнього ринку без погодження з їх виробниками).
                """
        },
        {
            "id": 3,
            "title": "Dell заробила багато грошей",
            "text": """Одна з найбільших компаній із виробництва компʼютерів та серверів Dell остаточно йде з ринку росії. Разом з тим корпорація звільняє весь штат співробітників там, пише Forbes з посиланням на російські медіа.

                Dell планує завершити роботу в рф наприкінці серпня. Компанія збиралася розвивати центр розробок у санкт-петербурзі, але тепер перемкнулася на центр розробок у Польщі.

                Загалом у російському представництві працюють близько 50 осіб. Dell може виплатити до восьми окладів співробітникам під час звільнення, а комусь залишать медстрахування на сімʼю до кінця року. Колишні працівники компанії кажуть, що техніку їм дозволили залишити собі, але всі дані корпорація видаляє із жорстких дисків та корпоративних телефонів.

                Видання пише, що, за словами гендиректора російської компанії з виробництва інноваційних рішень «Аеродиск» Вʼячеслава Володковича, вихід Dell змусить частину замовників перейти на російські рішення, «беручи на себе всі ризики, повʼязані з нестачею необхідних обсягів виробництва». Хтось шукатиме рішення в паралельному імпорті, тобто «сірому» ринку (у травні російський уряд дозволив компаніям ввозити товари для внутрішнього ринку без погодження з їх виробниками).
                """
        }
    ]
    last_id = 3

    def get_all(self):
        return self.storage

    def get_one(self, id_):
        for post in self.storage:
            if post["id"] == id_:
                return post

    def create(self, title, text):
        self.last_id += 1
        new_post = {
            "id": self.last_id,
            "title": title,
            "text": text
        }
        self.storage.append(new_post)
        return new_post

    def update(self, id_, title, text):
        post = {
            "id": id_,
            "title": title,
            "text": text
        }
        for i in range(len(self.storage)):
            if self.storage[i].get("id") == id_:
                self.storage[i] = post

        return post

    def delete(self, id_):
        self.storage = [post for post in self.storage if post["id"] != id_]
