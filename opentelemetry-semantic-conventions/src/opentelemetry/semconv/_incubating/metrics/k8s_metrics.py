# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import (
    Callable,
    Final,
    Generator,
    Iterable,
    Optional,
    Sequence,
    Union,
)

from opentelemetry.metrics import (
    CallbackOptions,
    Counter,
    Meter,
    ObservableGauge,
    Observation,
)

# pylint: disable=invalid-name
CallbackT = Union[
    Callable[[CallbackOptions], Iterable[Observation]],
    Generator[Iterable[Observation], CallbackOptions, None],
]

K8S_NODE_CPU_TIME: Final = "k8s.node.cpu.time"
"""
Total CPU time consumed
Instrument: counter
Unit: s
Note: Total CPU time consumed by the specific Node on all available CPU cores.
"""


def create_k8s_node_cpu_time(meter: Meter) -> Counter:
    """Total CPU time consumed"""
    return meter.create_counter(
        name=K8S_NODE_CPU_TIME,
        description="Total CPU time consumed",
        unit="s",
    )


K8S_NODE_CPU_USAGE: Final = "k8s.node.cpu.usage"
"""
Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs
Instrument: gauge
Unit: {cpu}
Note: CPU usage of the specific Node on all available CPU cores, averaged over the sample window.
"""


def create_k8s_node_cpu_usage(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"""
    return meter.create_observable_gauge(
        name=K8S_NODE_CPU_USAGE,
        callbacks=callbacks,
        description="Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs",
        unit="{cpu}",
    )


K8S_NODE_MEMORY_USAGE: Final = "k8s.node.memory.usage"
"""
Memory usage of the Node
Instrument: gauge
Unit: By
Note: Total memory usage of the Node.
"""


def create_k8s_node_memory_usage(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """Memory usage of the Node"""
    return meter.create_observable_gauge(
        name=K8S_NODE_MEMORY_USAGE,
        callbacks=callbacks,
        description="Memory usage of the Node",
        unit="By",
    )


K8S_NODE_NETWORK_ERRORS: Final = "k8s.node.network.errors"
"""
Node network errors
Instrument: counter
Unit: {error}
"""


def create_k8s_node_network_errors(meter: Meter) -> Counter:
    """Node network errors"""
    return meter.create_counter(
        name=K8S_NODE_NETWORK_ERRORS,
        description="Node network errors",
        unit="{error}",
    )


K8S_NODE_NETWORK_IO: Final = "k8s.node.network.io"
"""
Network bytes for the Node
Instrument: counter
Unit: By
"""


def create_k8s_node_network_io(meter: Meter) -> Counter:
    """Network bytes for the Node"""
    return meter.create_counter(
        name=K8S_NODE_NETWORK_IO,
        description="Network bytes for the Node",
        unit="By",
    )


K8S_NODE_UPTIME: Final = "k8s.node.uptime"
"""
The time the Node has been running
Instrument: gauge
Unit: s
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_k8s_node_uptime(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """The time the Node has been running"""
    return meter.create_observable_gauge(
        name=K8S_NODE_UPTIME,
        callbacks=callbacks,
        description="The time the Node has been running",
        unit="s",
    )


K8S_POD_CPU_TIME: Final = "k8s.pod.cpu.time"
"""
Total CPU time consumed
Instrument: counter
Unit: s
Note: Total CPU time consumed by the specific Pod on all available CPU cores.
"""


def create_k8s_pod_cpu_time(meter: Meter) -> Counter:
    """Total CPU time consumed"""
    return meter.create_counter(
        name=K8S_POD_CPU_TIME,
        description="Total CPU time consumed",
        unit="s",
    )


K8S_POD_CPU_USAGE: Final = "k8s.pod.cpu.usage"
"""
Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs
Instrument: gauge
Unit: {cpu}
Note: CPU usage of the specific Pod on all available CPU cores, averaged over the sample window.
"""


def create_k8s_pod_cpu_usage(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"""
    return meter.create_observable_gauge(
        name=K8S_POD_CPU_USAGE,
        callbacks=callbacks,
        description="Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs",
        unit="{cpu}",
    )


K8S_POD_MEMORY_USAGE: Final = "k8s.pod.memory.usage"
"""
Memory usage of the Pod
Instrument: gauge
Unit: By
Note: Total memory usage of the Pod.
"""


def create_k8s_pod_memory_usage(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """Memory usage of the Pod"""
    return meter.create_observable_gauge(
        name=K8S_POD_MEMORY_USAGE,
        callbacks=callbacks,
        description="Memory usage of the Pod",
        unit="By",
    )


K8S_POD_NETWORK_ERRORS: Final = "k8s.pod.network.errors"
"""
Pod network errors
Instrument: counter
Unit: {error}
"""


def create_k8s_pod_network_errors(meter: Meter) -> Counter:
    """Pod network errors"""
    return meter.create_counter(
        name=K8S_POD_NETWORK_ERRORS,
        description="Pod network errors",
        unit="{error}",
    )


K8S_POD_NETWORK_IO: Final = "k8s.pod.network.io"
"""
Network bytes for the Pod
Instrument: counter
Unit: By
"""


def create_k8s_pod_network_io(meter: Meter) -> Counter:
    """Network bytes for the Pod"""
    return meter.create_counter(
        name=K8S_POD_NETWORK_IO,
        description="Network bytes for the Pod",
        unit="By",
    )


K8S_POD_UPTIME: Final = "k8s.pod.uptime"
"""
The time the Pod has been running
Instrument: gauge
Unit: s
Note: Instrumentations SHOULD use a gauge with type `double` and measure uptime in seconds as a floating point number with the highest precision available.
The actual accuracy would depend on the instrumentation and operating system.
"""


def create_k8s_pod_uptime(
    meter: Meter, callbacks: Optional[Sequence[CallbackT]]
) -> ObservableGauge:
    """The time the Pod has been running"""
    return meter.create_observable_gauge(
        name=K8S_POD_UPTIME,
        callbacks=callbacks,
        description="The time the Pod has been running",
        unit="s",
    )