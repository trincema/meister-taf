import os, sys, inspect
from io import BytesIO
from pathlib import Path
from ..layer0_automation_tool.playwright.dvc import DoViewCheck

class SnapshotKeywords:
    
    def info_snapshot():
        """
        Take info snapshot and don't fail the tests in case the snapshots don't match up 100%.
        This method is useful for areas we know sometimes a few pixels might always be different,
        but we still want to have the snapshot comparison in place, just in case from time to time
        we want to have a look at them.
        """
        abs_path = os.path.abspath((inspect.stack()[1])[1])
        caller_path = os.path.dirname(abs_path)
        filepath = (
            Path(request.node.fspath).parent.resolve()
            / "__snapshots__"
            / browser_name
            / sys.platform
        )
        filepath.mkdir(parents=True, exist_ok=True)
        file = filepath / name
        if update_snapshot:
            file.write_bytes(img)
            return
        if not file.exists():
            pytest.fail("Snapshot not found, use --update-snapshots to update it.")
        image = Image.open(BytesIO(img))
        golden = Image.open(file)
        diff_pixels = pixelmatch(image, golden, threshold=threshold)
        assert diff_pixels == 0, "Snapshots does not match"
    
    def assert_snapshot(assert_snapshot):
        """Summary:
        Take snapshot and compare with previous snapshot.
        """
        assert_snapshot(DoViewCheck.page.screenshot())