import asyncio

class ElfoDomestico:
    TIEMPO_PREPARACION = {
        'pastel_calabaza': 5,
        'gusarajo': 3,
        'pocion_multijugos': 2,
        'cerveza_mantequilla': 1.5,
    }

    def __init__(self, pedidos, id):
        self.pedidos = pedidos
        self.id = id

    async def solicitar_pedidos(self):
        while not self.pedidos.empty():
            pedido = await self.pedidos.get()
            await self.solicitar_pedido(pedido)

    async def solicitar_pedido(self, pedido):
        print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido["id"]}] {"*" * 30}')
        for producto in pedido['productos']:
            await self.solicitar_producto(producto, pedido['id'])
        await self.despachar_pedido(pedido)

    async def solicitar_producto(self, producto, pedido_id):
        tiempo_espera = self.TIEMPO_PREPARACION[producto]
        print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido_id}] Solicitando {producto}. Esperando {tiempo_espera} seg...')
        await asyncio.sleep(tiempo_espera)
        print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido_id}] Producto listo: {producto}')

    async def despachar_pedido(self, pedido):
        print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido["id"]}] ¡Pedido despachado!')
        for producto in pedido['productos']:
            print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido["id"]}] Despachando {producto}')
        print(f'<Elfo Doméstico: {self.id}> [Pedido: {pedido["id"]}] {"-" * 30}\n')

async def main():
    cola_pedidos = asyncio.Queue()
    await cola_pedidos.put({'id': 1, 'productos': ['pastel_calabaza', 'gusarajo', 'pocion_multijugos']})
    await cola_pedidos.put({'id': 2, 'productos': ['cerveza_mantequilla']})

    elfo1 = ElfoDomestico(cola_pedidos, 1)
    elfo2 = ElfoDomestico(cola_pedidos, 2)

    tareas = [
        asyncio.create_task(elfo1.solicitar_pedidos()),
        asyncio.create_task(elfo2.solicitar_pedidos())
    ]

    await asyncio.gather(*tareas)

if __name__ == '__main__':
    asyncio.run(main())