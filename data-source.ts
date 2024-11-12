import "reflect-metadata"
import { DataSource } from "typeorm"
import { User } from "./entity/User"

export const AppDataSource = new DataSource({
    type: "postgres",
    host: "34.79.21.6",
    port: 5432,
    username: "root",
    password: "Valikf2005",
    database: "test",
    synchronize: true,
    logging: false,
    entities: [User],
    migrations: ['src/migration/**/*.ts'],
    subscribers: [],
})
