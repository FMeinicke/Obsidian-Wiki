---
{"publish":true,"created":"2025-05-15T09:01:50.373+02:00","modified":"2025-05-26T15:25:10.575+02:00","published":"2025-05-26T15:25:10.575+02:00","cssclasses":""}
---


#linux/usb/reset #linux/usb/unbind #linux/usb/bind

> [!info] Source
> 
> - <https://unix.stackexchange.com/a/704342/482223>

- it happened to me after a return from sleep that no plugged or unplugged devices were recognized
- I found the following script that goes through all USB controllers and resets them

```bash
#!/usr/bin/env bash
# Resets all USB host controllers of the system.
# This is useful in case one stopped working
# due to a faulty device having been connected to it.
# from https://unix.stackexchange.com/a/704342/482223

base="/sys/bus/pci/drivers"
sleep_secs="1"

# This might find a sub-set of these:
# * 'ohci_hcd' - USB 3.0
# * 'ehci-pci' - USB 2.0
# * 'xhci_hcd' - USB 3.0
echo "Looking for USB standards ..."
for usb_std in "$base/"?hci[-_]?c*
do
    echo "* USB standard '$usb_std' ..."
    for dev_path in "$usb_std/"*:*
    do
        dev="$(basename "$dev_path")"
        [ "$dev" == "*:*" ] && continue
        echo "  - Resetting device '$dev' ..."
        printf '%s' "$dev" | sudo tee "$usb_std/unbind" > /dev/null
        sleep "$sleep_secs"
        printf '%s' "$dev" | sudo tee "$usb_std/bind" > /dev/null
        echo "    done."
    done
    echo "  done."
done
echo "done."
```