from asyncio import gather
from application.ping.entities import HealthStatus
from application.ping.models import Ping


class PingManager:

    async def _perform_application_health_check(self) -> HealthStatus:
        """Perform application health check

        Ensure that the application is running

        Returns:
            HealthStatus: The health status of the application
        """
        return HealthStatus(name="application", is_healthy=True)

    async def _perform_db_health_check(self) -> HealthStatus:
        """Perform db health check

        Ensure that the db is running

        Returns:
            HealthStatus: The health status of redis
        """
        is_healthy = await Ping.raw("SELECT 1")
        return HealthStatus(name="MariaDB", is_healthy=bool(is_healthy))

    async def get_health_status(self) -> list[HealthStatus]:
        """Get health status

        Get the health status of the application
        """
        health = await gather(
            self._perform_application_health_check(),
            self._perform_db_health_check(),
        )

        return list(health)
